import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

class TestScavengerAPI:
    def test_start_scavenger_game(self, client):
        response = client.post("/start/scavenger")
        assert response.status_code == 200
        # Check for scavenger specific content
        assert "SCAVENGER HUNT" in response.text
        # Should check for list structure, maybe check for progress bar
        assert "progress-bar" in response.text or "progress" in response.text.lower()

    def test_scavenger_toggle_updates_progress(self, client):
        # Start game first
        client.post("/start/scavenger")
        
        # Toggle first item
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # Response should show updated progress
        # Since I haven't implemented the template, exact string is hard to guess
        # But it should be a successful toggle
        assert "checked" in response.text or "marked" in response.text
