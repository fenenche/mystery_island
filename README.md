

# Mystery Island: The Lost Lighthouse

## About the Game

Mystery Island is a Python command-line adventure game.

You are stranded on a mysterious island after a storm. Your mission is to find useful items, manage your energy, cross the Old Bridge, and restore the Lighthouse so that a rescue boat can find you.

## Requirements

- Python 3
- No external libraries are required.

## How to Run the Game

1. Open your terminal.
2. Navigate to the project folder.
3. Run:

```bash
python3 main.py
```

## Game Rules

- You start with 5 energy points.
- You begin at the Beach.
- Explore the five locations:
  - Beach
  - Jungle
  - Cave
  - Old Bridge
  - Lighthouse
- Find the rope in the Jungle.
- Find the lantern in the Cave.
- Use the rope to cross the Old Bridge.
- Use the lantern to restore the Lighthouse.
- Make careful decisions because different actions consume different amounts of energy.
- If your energy reaches zero before winning, the game ends.
- You can quit or choose to play again.

## How to Run Automated Tests

Run the following command:

```bash
python3 -m unittest discover -s tests -v
```

The automated tests check player creation, movement, item collection, invalid choices, energy management, bridge access, and winning conditions.

## Project Structure

```text
mystery_island/
│
├── main.py
├── game.py
├── README.md
│
└── tests/
    └── test_game.py
```

## Known Limitations

- The game runs in the terminal and does not have a graphical interface.
- Player progress is not saved between game sessions.
- The game uses a fixed set of locations and decisions.