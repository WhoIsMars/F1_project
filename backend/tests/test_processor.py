import pytest
from processor import process_data

def test_process_data_empty():
    raw = {}
    result = process_data(raw)
    assert result["race"] == ""
    assert result["lap"] == ""
    assert result["drivers"] == []

def test_process_data_valid():
    raw = {
        "race": "Monaco GP",
        "lap": 10,
        "drivers": [
            {"id": "verstappen", "position": 1, "lapTime": "1:15.000"},
            {"id": "leclerc", "position": 2, "lapTime": "1:15.200"},
        ]
    }
    result = process_data(raw)
    assert result["race"] == "Monaco GP"
    assert result["lap"] == 10
    assert len(result["drivers"]) == 2
    
    # Check win probability logic (inverse position)
    # Total drivers = 2
    # Pos 1: (2 - 1 + 1) / 2 * 100 = 100.0
    # Pos 2: (2 - 2 + 1) / 2 * 100 = 50.0
    
    d1 = result["drivers"][0]
    assert d1["id"] == "verstappen"
    assert d1["winProbability"] == 100.0
    
    d2 = result["drivers"][1]
    assert d2["id"] == "leclerc"
    assert d2["winProbability"] == 50.0
    
    # Check new fields
    assert "status" in result
    assert "weather" in result
    assert "condition" in result["weather"]
    assert "temp" in result["weather"]
    
    assert "pitStops" in d1
    assert "tyre" in d1
    assert d1["tyre"] in ["SOFT", "MEDIUM", "HARD"]
