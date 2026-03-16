from dataclasses import dataclass, field

from app.data import QUESTIONS
from app.game_logic import (
    check_bingo,
    generate_board,
    generate_scavenger_board,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    game_mode: GameMode = GameMode.BINGO
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    current_card: str | None = None

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def progress(self) -> float:
        """Calculate progress percentage for scavenger mode."""
        if not self.board:
            return 0.0
        marked_count = sum(1 for sq in self.board if sq.is_marked)
        return (marked_count / len(self.board)) * 100.0

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.game_mode = mode
        if mode == GameMode.SCAVENGER:
            self.board = generate_scavenger_board()
        elif mode == GameMode.CARD_DECK:
            self.board = []
            self.draw_card()
        else:
            self.board = generate_board()
            
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False

    def draw_card(self) -> str:
        """Draw a random card."""
        import random
        self.current_card = random.choice(QUESTIONS)
        return self.current_card

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state not in (GameState.PLAYING, GameState.BINGO):
            return
            
        self.board = toggle_square(self.board, square_id)
        self._check_win_condition()

    def _check_win_condition(self) -> None:
        """Check if the current board state satisfies the win condition for the current mode."""
        if self.game_mode == GameMode.BINGO:
            if self.winning_line is None:
                bingo = check_bingo(self.board)
                if bingo is not None:
                    self.winning_line = bingo
                    self.game_state = GameState.BINGO
                    self.show_bingo_modal = True
        
        elif self.game_mode == GameMode.SCAVENGER:
            if all(sq.is_marked for sq in self.board):
                self.game_state = GameState.COMPLETE

    def reset_game(self) -> None:
        self.game_state = GameState.START
        # Reset to defaults
        self.board = []
        self.current_card = None
        self.winning_line = None
        self.show_bingo_modal = False

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
