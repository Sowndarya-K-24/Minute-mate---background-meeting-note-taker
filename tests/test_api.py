from app import app  

def test_status_api():
    client = app.test_client()
    res = client.get("/status")
    assert res.status_code == 200
    assert res.json["state"] in ["recording", "idle"]

def test_minutes_api_mocked():
    client = app.test_client()
    res = client.get("/minutes/mock-id")
    assert res.status_code == 200
    assert "summary" in res.json
    assert "actions" in res.json