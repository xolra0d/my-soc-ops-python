from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_start_card_deck_game():
    # Start session
    client.get("/")
    
    # Start Card Deck mode
    response = client.post("/start/card-deck")
    assert response.status_code == 200
    
    # Check for title
    assert "CARD SHUFFLE" in response.text
    
    # Check for initial empty state
    assert "ACCESS TERMINAL" in response.text
    assert "TAP TO DECRYPT" in response.text
    
    # Ensure no card data is shown yet
    assert "TARGET_DATA" not in response.text

def test_draw_card():
    # Start session
    client.get("/")
    client.post("/start/card-deck")
    
    # Draw a card
    response = client.post("/draw-card")
    assert response.status_code == 200
    
    # Check for card data
    assert "TARGET_DATA" in response.text
    assert "AWAITING_INPUT" in response.text
    
    # Ensure empty state is gone
    assert "ACCESS TERMINAL" not in response.text

def test_reset_from_card_deck():
    # Start session
    client.get("/")
    client.post("/start/card-deck")
    
    # Reset
    response = client.post("/reset")
    assert response.status_code == 200
    
    # Check for start screen elements
    assert "INITIATE BINGO" in response.text
    assert "CARD SHUFFLE" in response.text
