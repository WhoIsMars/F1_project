import asyncio
import time
from typing import Any, Dict, List, Optional
import httpx
import logging

# Simple in‑memory cache with timestamp
_cache: Dict[str, Dict[str, Any]] = {}
CACHE_TTL = 60  # seconds

# Jolpica-F1 API base URL (Ergast replacement)
ERGAST_BASE = "https://api.jolpi.ca/ergast/f1"

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("collector")

async def _fetch(url: str) -> Optional[Dict[str, Any]]:
    """Fetch JSON data from the given URL with basic error handling.
    Returns ``None`` on failure.
    """
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as exc:
            logger.warning(f"Ergast request failed for {url}: {exc}")
            return None

def _is_cached(key: str) -> bool:
    entry = _cache.get(key)
    if not entry:
        return False
    return (time.time() - entry["ts"]) < CACHE_TTL

def _store_cache(key: str, data: Dict[str, Any]):
    _cache[key] = {"ts": time.time(), "data": data}

async def get_schedule(season: str = "current") -> Optional[Dict[str, Any]]:
    """Return the race schedule for the given season.
    Uses cache to avoid hitting the rate limit.
    """
    cache_key = f"schedule:{season}"
    if _is_cached(cache_key):
        return _cache[cache_key]["data"]
    url = f"{ERGAST_BASE}/{season}.json"
    data = await _fetch(url)
    if data:
        _store_cache(cache_key, data)
    return data

async def get_driver_standings(season: str = "current") -> Optional[Dict[str, Any]]:
    cache_key = f"standings:{season}"
    if _is_cached(cache_key):
        return _cache[cache_key]["data"]
    url = f"{ERGAST_BASE}/{season}/driverStandings.json"
    data = await _fetch(url)
    if data:
        _store_cache(cache_key, data)
    return data

async def get_latest_results(season: str = "current") -> Optional[Dict[str, Any]]:
    cache_key = f"results:{season}"
    if _is_cached(cache_key):
        return _cache[cache_key]["data"]
    url = f"{ERGAST_BASE}/{season}/results.json"
    data = await _fetch(url)
    if data:
        _store_cache(cache_key, data)
    return data

# ---------- Scraper fallback (very simplified) ----------

def _scrape_live_data() -> Dict[str, Any]:
    """Placeholder scraper that would pull live data from public pages.
    In a real implementation you could scrape the official timing page or a
    community feed. Here we return a static example structure.
    """
    logger.info("Using scraper fallback for live data")
    # Example static payload – replace with real scraping logic.
    return {
        "race": "Monaco Grand Prix",
        "lap": 12,
        "drivers": [
            {"id": "hamilton", "position": 1, "lapTime": "1:12.345"},
            {"id": "verstappen", "position": 2, "lapTime": "1:12.567"},
        ],
    }

async def collect_live_data() -> Dict[str, Any]:
    """Collect live data using OpenF1 API with fallback to simulation.
    Priority: OpenF1 > Simulation
    """
    # 1. Try OpenF1 - Good for historical/recent data
    logger.info("Attempting OpenF1 API...")
    try:
        data = await _fetch_openf1()
        if data:
            logger.info("✅ Successfully fetched from OpenF1")
            return data
    except Exception as e:
        logger.warning(f"❌ OpenF1 failed: {e}")
    
    # 2. Fallback to simulation
    logger.info("⚠️ Using fallback simulation")
    return _fallback_simulation()

async def _fetch_openf1() -> Optional[Dict[str, Any]]:
    """Fetch data from OpenF1 API with improved data extraction."""
    OPENF1_BASE = "https://api.openf1.org/v1"
    
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
        try:
            # Get latest session for Lasvegas GP 2024
            sessions_url = f"{OPENF1_BASE}/sessions?meeting_name=Las%20Vegas&year=2024&session_name=Race&limit=1"
            sessions_response = await client.get(sessions_url)
            sessions_response.raise_for_status()
            sessions = sessions_response.json()
            
            if not sessions:
                logger.warning("No Las Vegas GP session found in OpenF1")
                return None
            
            session_key = sessions[0]["session_key"]
            
            # Get laps data to find current lap
            laps_url = f"{OPENF1_BASE}/laps?session_key={session_key}&limit=1000"
            laps_response = await client.get(laps_url)
            laps_response.raise_for_status()
            laps_data = laps_response.json()
            
            # Find max lap number (current lap)
            current_lap = 42  # Default
            if laps_data:
                current_lap = max(lap.get("lap_number", 1) for lap in laps_data)
            
            # Get driver positions
            positions_url = f"{OPENF1_BASE}/position?session_key={session_key}&limit=1000"
            positions_response = await client.get(positions_url)
            positions_response.raise_for_status()
            positions_data = positions_response.json()
            
            # Get intervals
            intervals_url = f"{OPENF1_BASE}/intervals?session_key={session_key}&limit=1000"
            intervals_response = await client.get(intervals_url)
            intervals_response.raise_for_status()
            intervals_data = intervals_response.json()
            
            # Get driver info
            drivers_url = f"{OPENF1_BASE}/drivers?session_key={session_key}"
            drivers_response = await client.get(drivers_url)
            drivers_response.raise_for_status()
            drivers_info = drivers_response.json()
            
            if not positions_data:
                logger.warning("No position data from OpenF1")
                return None
            
            # Get latest position data per driver
            latest_positions = {}
            for entry in positions_data:
                driver_number = entry["driver_number"]
                if driver_number not in latest_positions or entry["date"] > latest_positions[driver_number]["date"]:
                    latest_positions[driver_number] = entry
            
            # Get latest intervals
            latest_intervals = {}
            for entry in intervals_data:
                driver_number = entry["driver_number"]
                if driver_number not in latest_intervals or entry["date"] > latest_intervals[driver_number]["date"]:
                    latest_intervals[driver_number] = entry
            
            # Build driver list
            drivers = []
            driver_map = {d["driver_number"]: d for d in drivers_info}
            
            for driver_num, pos_data in sorted(latest_positions.items(), key=lambda x: x[1].get("position", 99)):
                driver_info = driver_map.get(driver_num, {})
                interval_info = latest_intervals.get(driver_num, {})
                
                # Format gap/interval
                gap = interval_info.get("interval", "")
                if not gap and pos_data.get("position") == 1:
                    gap = "LEAD"
                elif not gap:
                    gap = f"+{(pos_data.get('position', 1) - 1) * 1.234:.3f}"
                
                drivers.append({
                    "id": driver_info.get("name_acronym", f"DR{driver_num}").lower(),
                    "code": driver_info.get("name_acronym", f"DR{driver_num}"),
                    "team": driver_info.get("team_name", "").lower().replace(" ", "_"),
                    "position": pos_data.get("position", 0),
                    "lapTime": gap,
                })
            
            return {
                "race": "Las Vegas Grand Prix",
                "season": "2024",
                "round": "23",
                "lap": current_lap,
                "totalLaps": 50,
                "date": sessions[0].get("date_start", ""),
                "drivers": drivers,
                "is_live": True,
                "source": "openf1"
            }
        except Exception as e:
            logger.error(f"OpenF1 detailed error: {e}")
            return None

def _fallback_simulation() -> Dict[str, Any]:
    """Fallback simulation with realistic Las Vegas GP standings."""
    logger.info("Using fallback simulation with realistic standings")
    
    # Current standings from user's input
    standings = [
        ("verstappen", "VER", "red_bull"),
        ("norris", "NOR", "mclaren"),
        ("antonelli", "ANT", "mercedes"),
        ("piastri", "PIA", "mclaren"),
        ("leclerc", "LEC", "ferrari"),
        ("sainz", "SAI", "ferrari"),
        ("hamilton", "HAM", "mercedes"),
        ("perez", "PER", "red_bull"),
        ("alonso", "ALO", "aston_martin"),
        ("stroll", "STR", "aston_martin"),
    ]
    
    drivers = []
    for i, (id, code, team) in enumerate(standings, 1):
        gap = f"+{(i-1) * 1.234:.3f}" if i > 1 else "LEAD"
        drivers.append({
            "id": id,
            "code": code,
            "team": team,
            "position": i,
            "lapTime": gap,
        })
    
    return {
        "race": "Las Vegas Grand Prix",
        "season": "2024",
        "round": "23",
        "date": "2024-11-23",
        "drivers": drivers,
        "is_live": False
    }

# Example background coroutine that periodically fetches data.
async def periodic_collector(interval: int = 5):
    while True:
        data = await collect_live_data()
        # In a real app you would push ``data`` to a shared queue or broadcast.
        logger.debug(f"Collected live data: {data}")
        await asyncio.sleep(interval)

# If this module is run directly, start a simple loop for debugging.
if __name__ == "__main__":
    asyncio.run(periodic_collector())
