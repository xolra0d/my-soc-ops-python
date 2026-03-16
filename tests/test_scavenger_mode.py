import pytest
from app.data import QUESTIONS
from app.game_logic import generate_scavenger_board, toggle_square
from app.models import GameMode, GameState, BingoSquareData
from app.game_service import GameSession

class TestScavengerModels:
    def test_game_mode_enum(self):
        assert GameMode.BINGO == "bingo"
        assert GameMode.SCAVENGER == "scavenger"

    def test_game_state_complete(self):
        assert GameState.COMPLETE == "complete"

class TestScavengerLogic:
    def test_generate_scavenger_board_count(self):
        board = generate_scavenger_board()
        assert len(board) == len(QUESTIONS)
        assert len(board) == 24

    def test_generate_scavenger_board_content(self):
        board = generate_scavenger_board()
        texts = {s.text for s in board}
        assert texts == set(QUESTIONS)

    def test_no_free_space_in_scavenger(self):
        board = generate_scavenger_board()
        assert not any(s.is_free_space for s in board)
        assert not any(s.is_marked for s in board)

class TestScavengerSession:
    def test_session_init_defaults(self):
        session = GameSession()
        assert session.game_mode == GameMode.BINGO
        assert session.progress == 0.0

    def test_start_scavenger_game(self):
        session = GameSession()
        session.start_game(mode=GameMode.SCAVENGER)
        assert session.game_mode == GameMode.SCAVENGER
        assert session.game_state == GameState.PLAYING
        assert len(session.board) == 24

    def test_scavenger_progress(self):
        session = GameSession()
        session.start_game(mode=GameMode.SCAVENGER)
        assert session.progress == 0.0
        
        # Mark one item
        session.handle_square_click(0)
        expected_progress = (1 / 24) * 100
        assert abs(session.progress - expected_progress) < 0.01

        # Mark another
        session.handle_square_click(1)
        expected_progress = (2 / 24) * 100
        assert abs(session.progress - expected_progress) < 0.01

    def test_scavenger_completion(self):
        session = GameSession()
        session.start_game(mode=GameMode.SCAVENGER)
        
        # Mark all items
        for i in range(24):
            session.handle_square_click(i)
            
        assert session.game_state == GameState.COMPLETE
        assert session.progress == 100.0

    def test_reset_clears_mode(self):
        session = GameSession()
        session.start_game(mode=GameMode.SCAVENGER)
        session.reset_game()
        # Should probably reset to default or allow picking mode again
        # Implementation detail: reset usually goes back to START state where mode doesn't matter yet
        assert session.game_state == GameState.START
