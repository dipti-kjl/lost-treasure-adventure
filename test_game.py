"""
Tests for The Lost Treasure Adventure.

Run them with:   python -m pytest -v

How these tests work:
    The game uses input() to talk to the player. In a test there is no player,
    so we use pytest's "monkeypatch" to replace input() with a fake that hands
    out pre-written answers one by one. Then we check what the game returns.
"""

import pytest

import game


def feed_inputs(monkeypatch, answers):
    """Replace input() with a fake that returns the given answers in order."""
    answer_iterator = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answer_iterator))


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def test_ask_choice_accepts_valid_answer(monkeypatch):
    feed_inputs(monkeypatch, ["left"])
    assert game.ask_choice("? ", ["left", "right"]) == "left"


def test_ask_choice_ignores_case_and_spaces(monkeypatch):
    feed_inputs(monkeypatch, ["  RIGHT  "])
    assert game.ask_choice("? ", ["left", "right"]) == "right"


def test_ask_choice_asks_again_after_invalid_answers(monkeypatch, capsys):
    feed_inputs(monkeypatch, ["banana", "", "right"])
    assert game.ask_choice("? ", ["left", "right"]) == "right"
    assert "Please type one of" in capsys.readouterr().out


@pytest.mark.parametrize("typed, expected", [
    ("yes", True), ("y", True), ("YES", True), (" Y ", True),
    ("no", False), ("n", False), ("NO", False),
])
def test_ask_yes_no(monkeypatch, typed, expected):
    feed_inputs(monkeypatch, [typed])
    assert game.ask_yes_no("? ") is expected


def test_ask_yes_no_retries_on_invalid_answer(monkeypatch):
    feed_inputs(monkeypatch, ["maybe", "yes"])
    assert game.ask_yes_no("? ") is True


def test_ask_name_rejects_empty_names(monkeypatch):
    feed_inputs(monkeypatch, ["", "   ", "  Asha  "])
    assert game.ask_name() == "Asha"


# ---------------------------------------------------------------------------
# Story paths: every ending of the game
# ---------------------------------------------------------------------------

def test_bridge_cross_wins(monkeypatch):
    feed_inputs(monkeypatch, ["cross"])
    assert game.bridge_path() is True


def test_bridge_swim_loses(monkeypatch):
    feed_inputs(monkeypatch, ["swim"])
    assert game.bridge_path() is False


def test_cave_glow_tunnel_wins(monkeypatch):
    feed_inputs(monkeypatch, ["glow"])
    assert game.cave_path() is True


def test_cave_growl_then_hide_wins(monkeypatch):
    feed_inputs(monkeypatch, ["growl", "hide"])
    assert game.cave_path() is True


def test_cave_growl_then_fight_loses(monkeypatch):
    feed_inputs(monkeypatch, ["growl", "fight"])
    assert game.cave_path() is False


def test_cave_survives_invalid_answers(monkeypatch):
    # Wrong answers must not crash the game; it simply asks again.
    feed_inputs(monkeypatch, ["up", "growl", "run away", "hide"])
    assert game.cave_path() is True


# ---------------------------------------------------------------------------
# A full round: left/right choice leads to the right path
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("answers, expected", [
    (["left", "glow"], True),
    (["left", "growl", "hide"], True),
    (["left", "growl", "fight"], False),
    (["right", "cross"], True),
    (["right", "swim"], False),
])
def test_play_adventure_all_endings(monkeypatch, answers, expected):
    feed_inputs(monkeypatch, answers)
    assert game.play_adventure("Tester") is expected


def test_play_adventure_mentions_player_name(monkeypatch, capsys):
    feed_inputs(monkeypatch, ["right", "cross"])
    game.play_adventure("Priya")
    assert "Priya" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# The whole program: main()
# ---------------------------------------------------------------------------

def test_main_player_declines_to_start(monkeypatch, capsys):
    feed_inputs(monkeypatch, ["Sam", "no"])
    game.main()
    output = capsys.readouterr().out
    assert "Sam" in output
    assert "Thanks for playing" in output


def test_main_lose_then_play_again_then_win(monkeypatch, capsys):
    feed_inputs(monkeypatch, [
        "Ravi",          # name
        "yes",           # start the adventure
        "right", "swim", # round 1: lose
        "y",             # play again
        "right", "cross",# round 2: win
        "no",            # stop playing
    ])
    game.main()
    output = capsys.readouterr().out
    assert "GAME OVER" in output
    assert "TRY AGAIN" in output
    assert "YOU WIN" in output
    assert "Treasures found: 1" in output
    assert "Adventures lost: 1" in output
    assert "Thanks for playing, Ravi!" in output


def test_main_win_then_quit(monkeypatch, capsys):
    feed_inputs(monkeypatch, ["Mia", "yes", "left", "glow", "no"])
    game.main()
    output = capsys.readouterr().out
    assert "YOU WIN" in output
    assert "GAME OVER" not in output
    assert "Thanks for playing, Mia!" in output
