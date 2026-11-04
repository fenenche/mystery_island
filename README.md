# Mystery Island: The Lost Lighthouse

## About the Game

Mystery Island is a Python command-line adventure game.

You are stranded on a mysterious island after a storm. Your mission is to find useful items, manage your energy, cross the Old Bridge, and restore the Lighthouse so that a rescue boat can find you.

## Objective

Explore the island, collect the required items, make careful decisions, and restore the Lighthouse before you run out of energy.

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
- You can explore five locations:
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

## Energy System and Player Decisions

Energy is limited, so every decision matters.

| Action | Energy Cost or Reward |
|---|---|
| Search the Beach wreckage | Costs 1 energy but rewards 2 energy |
| Enter the Jungle | Costs 1 energy |
| Take the safe path to the Cave | Costs 1 energy |
| Take the dangerous shortcut | Costs 2 energy |
| Search the Cave carefully | Costs 1 energy |
| Search the Cave quickly | Costs 2 energy |
| Cross the Old Bridge | Costs 1 energy |
| Restore the Lighthouse | Costs 1 energy |

Searching the Beach wreckage is optional, but it helps you gain energy.

**Recommended winning strategy:**
1. Search the Beach wreckage.
2. Enter the Jungle and collect the rope.
3. Choose the safe path to the Cave.
4. Search the Cave carefully and collect the lantern.
5. Cross the Old Bridge.
6. Restore the Lighthouse.

This route allows you to complete the game with 1 energy point remaining.

## Winning and Losing

**Winning:**
- Collect the rope and lantern.
- Reach the Lighthouse through the Old Bridge.
- Restore the Lighthouse.
- A rescue boat arrives, and you win.

**Losing:**
- If your energy reaches zero before you restore the Lighthouse, the game ends.

**Quitting:**
- You can leave the game at any time by selecting Quit.
- After a game ends, you can choose whether to play again.

## How to Run Automated Tests

Run the following command:

```bash
python3 -m unittest discover -s tests -v
```

The automated tests check:
- Player creation.
- Movement between locations.
- Item collection.
- Invalid movement and choices.
- Energy management.
- Bridge access.
- Lighthouse restoration.
- Winning conditions.

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
- Energy cannot be replenished repeatedly; the Beach wreckage can only be searched once per game.