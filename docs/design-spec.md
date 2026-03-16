# Design Spec: Card Deck Shuffle Mode

## Overview
A new game mode where players can draw random cards with questions.

## User Flow
1. User opens the game.
2. User selects "Card Deck Shuffle" mode.
3. User sees a card (initially face down or with a prompt).
4. User taps the card/screen.
5. A random question appears on the card.
6. User can tap again to get a new card (shuffle/draw).

## UI/UX
- **Start Screen**: Add a new button for "Card Deck Shuffle".
- **Game Screen**:
    - A central card element.
    - Animation for flipping/drawing a card.
    - Display the question text clearly.
    - "Next Card" or tap interaction.

## Technical Details
- **Route**: `/start/card-deck`
- **Game Mode**: `GameMode.CARD_DECK`
- **State**: `current_card` (str)
- **Data**: Reuse `QUESTIONS` from `app/data.py` for now.

## Todo
- [x] Add `GameMode.CARD_DECK`
- [x] Add `draw_card` logic to `GameSession`
- [x] Create `card_deck.html` template
- [x] Add routes
- [x] Style the card
- [x] Update tests and fix scavenger test issues

