import sys
import os

# Add project root to Python path (works in CI and Windows)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from src.app import app


def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "HealthyLife Tracker is running"


def test_add_and_get_records():
    client = app.test_client()

    sample = {
        "date": "2025-01-01",
        "activity": "running",
        "duration": 30,
        "water_intake": 500,
        "sleep_hours": 7
    }

    res_add = client.post("/add", json=sample)
    assert res_add.status_code == 200

    res_get = client.get("/records")
    assert res_get.status_code == 200
    assert isinstance(res_get.json, list)
    assert len(res_get.json) >= 1
