# 🗺️ The Lost Treasure Adventure

A colorful, interactive **choose-your-own-adventure game** that runs in the terminal, built with beginner-friendly Python.

You explore a mysterious forest looking for hidden treasure. Every choice changes the story: some paths lead to gold, others to a very bad day with an alligator.

> Bonus: `web/index.html` is a browser version of the same game (see [Web version](#web-version)).

## Overview

This project started as a tiny five-line adventure and grew into a complete command-line game. It focuses on clean, readable code: small functions, clear names, input validation and automated tests. It uses only core Python plus one small library for colors.

## Features

- Colorful title screen with decorative borders and emojis
- Personal welcome using the player's name
- Branching story with **5 different endings** (3 wins, 2 losses)
- Colored **YOU WIN**, **GAME OVER** and **TRY AGAIN** screens
- Input validation: wrong answers, empty answers, capital letters and extra spaces never crash the game
- Play again without restarting the program, with a running score
- Friendly goodbye message with the player's name
- Automated tests with `pytest`

## Technologies used

| Tool | Purpose |
| --- | --- |
| Python 3.8+ | Game logic (developed and tested on 3.13) |
| [colorama](https://pypi.org/project/colorama/) | Colored text in the terminal, also on Windows |
| [pytest](https://pytest.org) | Automated tests (development only) |

Python concepts used: variables, `input()` / `print()`, `if` / `elif` / `else`, `while` loops, string methods (`strip()`, `lower()`, `center()`), functions, f-strings.

## Folder structure

```
lost-treasure-adventure/
├── game.py                # The game (all code, fully commented)
├── test_game.py           # Automated tests
├── requirements.txt       # Runtime dependency: colorama
├── requirements-dev.txt   # Adds pytest for running the tests
├── README.md              # This file
├── .gitignore             # Files Git should ignore
├── screenshots/           # Put your screenshots here
│   └── .gitkeep
└── web/
    └── index.html         # Optional browser version of the game
```

## Installation

You need [Python 3.8 or newer](https://www.python.org/downloads/) and Git.

```bash
# 1. Get the code
git clone https://github.com/<your-username>/lost-treasure-adventure.git
cd lost-treasure-adventure

# 2. (Recommended) create a virtual environment
python -m venv venv

# Activate it:
#   Windows (PowerShell):  venv\Scripts\Activate.ps1
#   Windows (cmd):         venv\Scripts\activate.bat
#   macOS / Linux:         source venv/bin/activate

# 3. Install the dependency
pip install -r requirements.txt
```

On macOS and Linux you may need to type `python3` and `pip3` instead of `python` and `pip`.

## How to run the project

```bash
python game.py
```

Type your answers and press Enter. Capital letters and extra spaces are fine.

If emojis look broken on Windows, use **Windows Terminal** instead of the old Command Prompt.

### Run the tests

```bash
pip install -r requirements-dev.txt
python -m pytest -v
```

The tests replace `input()` with pre-written answers, so every ending, the input validation and the play-again loop are checked automatically.

## Screenshots

Run the game, take a screenshot of each screen, save the images in the `screenshots/` folder and replace the lines below with real image links:

<!--
![Welcome screen](screenshots/welcome.png)
![Cave path](screenshots/cave.png)
![You win](screenshots/win.png)
![Game over](screenshots/game-over.png)
-->

*Screenshots coming soon.*

## Story map

```
Forest path
├── LEFT  → Dark cave
│           ├── glow tunnel  → Treasure chest        🏆 WIN
│           └── growl tunnel → Cave creature
│                              ├── hide  → Chest behind it   🏆 WIN
│                              └── fight → Chased away       💀 GAME OVER
└── RIGHT → Old bridge
            ├── cross → Hidden treasure              🏆 WIN
            └── swim  → Alligator                    💀 GAME OVER
```

## Web version

`web/index.html` is a single file with no build step. It follows the same story, choices and validation as `game.py`, and works as a browser terminal. To try it, open the file in a browser. To publish it for free, turn on **GitHub Pages** in your repository settings and serve the `web/` folder or move `index.html` to the repository root.

## Future improvements

- Add more story branches and a longer forest map
- Add an inventory system (pick up a torch, a key or a map)
- Add health points and random events
- Save high scores to a file
- Add short pauses for a typewriter effect
- Add sound effects
- Package the game so it installs with `pip`

## License

Add a license of your choice (for example MIT) before sharing the project publicly.
