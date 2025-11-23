# F1 Live Stats - Setup Guide

## Quick Start

### 1. Install Dependencies

**Backend:**
```bash
cd backend
pip install fastapi uvicorn httpx websockets
```

**Frontend:**
```bash
cd frontend
npm install
```

### 2. Configure Live Data API (Optional but Recommended)

For **real live data**, you need a Formula Live Pulse API key:

1. Go to [RapidAPI - Formula Live Pulse](https://rapidapi.com/formula-live-pulse/api/formula-live-pulse)
2. Subscribe to a plan (starts at basic/free tier)
3. Copy your API key
4. Edit `backend/config.py`:
   ```python
   RAPIDAPI_KEY = "your-api-key-here"
   ```

**Without an API key**, the app will use:
- OpenF1 (historical data)
- Fallback simulation (accurate standings but simulated telemetry)

### 3. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Open:** http://localhost:5173

## Data Sources (Priority Order)

1. **Formula Live Pulse** (RapidAPI) - ✅ Best for live data
   - Real-time timing, positions, gaps
   - Pit stops, tyre compounds
   - Race control messages
   - **Requires:** API key

2. **OpenF1** - ✅ Good for historical data
   - Free for past sessions
   - ~3s delay for live (paid tier)
   - **Requires:** Nothing (free tier)

3. **Simulation Fallback** - ✅ Always available
   - Based on real race standings
   - Realistic lap progression
   - **Requires:** Nothing

## Features

- ✅ Real-time driver positions
- ✅ Live lap times and gaps
- ✅ Tyre compound display
- ✅ Animated track map
- ✅ Weather and track conditions
- ✅ Sector times visualization
- ✅ Responsive design (no scroll)

## Troubleshooting

**Backend not connecting?**
- Check if uvicorn is running on port 8000
- Verify WebSocket connection in browser console

**No live data?**
- Add your RapidAPI key to `backend/config.py`
- Check API subscription status
- Fallback simulation will activate automatically

**Frontend not loading?**
- Ensure npm run dev is running on port 5173
- Clear browser cache
- Check console for errors
