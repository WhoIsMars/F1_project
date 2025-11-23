import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from collector import collect_live_data, get_schedule

@pytest.mark.asyncio
async def test_get_schedule_success():
    mock_response = {
        "MRData": {
            "RaceTable": {
                "Races": [{"raceName": "Bahrain GP"}]
            }
        }
    }
    
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        # Create a MagicMock for the response (synchronous methods like json() and raise_for_status())
        mock_response_obj = MagicMock()
        mock_response_obj.status_code = 200
        mock_response_obj.json.return_value = mock_response
        
        # The await client.get() returns this response object
        mock_get.return_value = mock_response_obj
        
        data = await get_schedule("2024")
        assert data["MRData"]["RaceTable"]["Races"][0]["raceName"] == "Bahrain GP"

@pytest.mark.asyncio
async def test_collect_live_data_fallback():
    # Mock get_latest_results to return None or empty to trigger fallback
    with patch("collector.get_latest_results", new_callable=AsyncMock) as mock_results:
        mock_results.return_value = None
        
        # This should trigger _scrape_live_data (the fallback)
        data = await collect_live_data()
        
        # The fallback currently returns a static "Monaco Grand Prix"
        assert data["race"] == "Monaco Grand Prix"
        assert len(data["drivers"]) > 0
