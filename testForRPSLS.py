# test_rpsls.py
import builtins
import types
import pytest

# Import the game and art modules
import rockPaperScissorsLizardSpock as game
from ascii_images import AsciiArt


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    # Make time.sleep a no-op to speed up tests
    monkeypatch.setattr(game.time, "sleep", lambda *_args, **_kwargs: None)


@pytest.fixture
def reset_delay(monkeypatch):
    # Ensure consistent delay for countdown logic
    monkeypatch.setattr(game, "delayA", 0.1)


def test_enums_and_constants_exist():
    # Ensure Action enum is defined and contains the expected members
    assert isinstance(game.Action.Rock.value, int)
    assert {a.name for a in game.Action} == {"Rock", "Paper", "Scissors", "Lizard", "Spock"}
    assert len(game.victories) == 5
    assert len(game.victory_explanations) == 10

    # Check taunts and quotes non-empty
    assert len(game.computer_taunts) > 0
    assert len(game.victory_quotes) > 0
    assert len(game.defeat_quotes) > 0
    assert len(game.tie_quotes) > 0


def test_ascii_art_structures_present():
    # Validate that key ASCII art attributes exist and are non-empty
    assert isinstance(AsciiArt.GAME_TITLE, str) and len(AsciiArt.GAME_TITLE.strip()) > 0
    assert isinstance(AsciiArt.ROCK, str) and len(AsciiArt.ROCK.strip()) > 0
    assert isinstance(AsciiArt.PAPER, str) and len(AsciiArt.PAPER.strip()) > 0
    assert isinstance(AsciiArt.SCISSORS, str) and len(AsciiArt.SCISSORS.strip()) > 0
    assert isinstance(AsciiArt.LIZARD, str) and len(AsciiArt.LIZARD.strip()) > 0
    assert isinstance(AsciiArt.SPOCK, str) and len(AsciiArt.SPOCK.strip()) > 0
    assert isinstance(AsciiArt.TIE_SCENE, str) and len(AsciiArt.TIE_SCENE.strip()) > 0
    assert isinstance(AsciiArt.GOODBYE_SCENE, str) and len(AsciiArt.GOODBYE_SCENE.strip()) > 0

    # Battle scenes should be a dict mapping tuples of two IntEnum-compatible values to strings
    assert isinstance(AsciiArt.BATTLE_SCENES, dict)
    for k, v in AsciiArt.BATTLE_SCENES.items():
        assert isinstance(k, tuple) and len(k) == 2
        assert isinstance(v, str) and len(v.strip()) > 0


def test_showActionArt_prints_expected_art(capsys):
    for action, art_attr in [
        (game.Action.Rock, "ROCK"),
        (game.Action.Paper, "PAPER"),
        (game.Action.Scissors, "SCISSORS"),
        (game.Action.Lizard, "LIZARD"),
        (game.Action.Spock, "SPOCK"),
    ]:
        game.showActionArt(action)
        out = capsys.readouterr().out
        art = getattr(AsciiArt, art_attr)
        assert art.strip() in out


def test_countDown_sequence(reset_delay, capsys):
    game.countDown()
    out = capsys.readouterr().out
    # Ensure all items and the SHOOT line appear in order
    expected = ["**Rock**", "**Paper**", "**Scissors**", "**Lizard**", "**Spock**", "💥 SHOOT! 💥"]
    idx = 0
    for line in out.splitlines():
        if idx < len(expected) and expected[idx] in line:
            idx += 1
    assert idx == len(expected)


def test_getUserSelection_reads_input_and_maps_enum(monkeypatch, capsys):
    # Fix the taunt to be deterministic
    monkeypatch.setattr(game.random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(builtins, "input", lambda prompt="": "0")  # Rock
    action = game.getUserSelection()
    assert action == game.Action.Rock
    out = capsys.readouterr().out
    assert "Enter your choice" in out
    assert game.computer_taunts[0] in out


def test_getComputerSelection_uses_random(monkeypatch):
    # Force the computer to choose Scissors (2)
    monkeypatch.setattr(game.random, "randint", lambda a, b: 2)
    comp = game.getComputerSelection()
    assert comp == game.Action.Scissors


@pytest.mark.parametrize(
    "user,comp,expected_phrase,expected_result_line",
    [
        # Wins
        (game.Action.Scissors, game.Action.Paper, "Scissors cuts paper", "YOU WIN!"),
        (game.Action.Paper, game.Action.Rock, "Paper covers rock", "YOU WIN!"),
        (game.Action.Rock, game.Action.Lizard, "Rock crushes lizard", "YOU WIN!"),
        (game.Action.Lizard, game.Action.Spock, "Lizard poisons Spock", "YOU WIN!"),
        (game.Action.Spock, game.Action.Scissors, "Spock smashes scissors", "YOU WIN!"),
        # Losses (reverse the above)
        (game.Action.Paper, game.Action.Scissors, "Scissors cuts paper", "YOU LOSE!"),
        (game.Action.Rock, game.Action.Paper, "Paper covers rock", "YOU LOSE!"),
        (game.Action.Lizard, game.Action.Rock, "Rock crushes lizard", "YOU LOSE!"),
        (game.Action.Spock, game.Action.Lizard, "Lizard poisons Spock", "YOU LOSE!"),
        (game.Action.Scissors, game.Action.Spock, "Spock smashes scissors", "YOU LOSE!"),
    ],
)
def test_determineWinner_win_loss_paths(user, comp, expected_phrase, expected_result_line, capsys):
    game.determineWinner(user, comp)
    out = capsys.readouterr().out
    # Headers show user and computer choices
    assert "YOU CHOSE" in out and user.name.upper() in out
    assert "COMPUTER CHOSE" in out and comp.name.upper() in out
    # Explanation and result
    assert expected_phrase.upper() in out
    assert expected_result_line in out


def test_determineWinner_tie_path(capsys):
    user = game.Action.Lizard
    comp = game.Action.Lizard
    game.determineWinner(user, comp)
    out = capsys.readouterr().out
    assert "TIE" in out or "It's a tie!" in out
    assert "Both players selected Lizard" in out


def test_victories_and_explanations_are_consistent():
    # Every rule in 'victories' should have a corresponding explanation
    missing = []
    for winner, losers in game.victories.items():
        for loser in losers:
            if (winner, loser) not in game.victory_explanations:
                missing.append((winner, loser))
    assert not missing, f"Missing explanations for: {missing}"

    # And there should be 10 unique directed explanations
    assert len(game.victory_explanations) == 10


def test_showBattleScene_uses_art_when_available(capsys):
    # Use a known pair that exists in AsciiArt.BATTLE_SCENES
    user = game.Action.Rock
    loser = game.Action.Scissors
    game.showBattleScene(user, loser)
    out = capsys.readouterr().out
    assert "ROCK CRUSHES SCISSORS" in out or "💥" in out


def test_printBanner_includes_rules_and_title(capsys):
    game.printBanner()
    out = capsys.readouterr().out
    assert "As seen on 'The Big Bang Theory'" in out
    assert "Scissors cuts Paper" in out
    assert "Rock crushes Lizard" in out
    assert AsciiArt.GAME_TITLE.strip().splitlines()[0].strip() in out


def test_main_one_round_win_then_exit(monkeypatch, capsys, reset_delay):
    # Simulate input:
    # - Choose Spock (4)
    # - Computer forced Scissors (2) => Spock beats Scissors (win)
    # - Play again? 'n'
    inputs = iter(["4", "n"])
    monkeypatch.setattr(builtins, "input", lambda _prompt="": next(inputs))
    monkeypatch.setattr(game.random, "randint", lambda a, b: 2)
    # Fix random.choice for deterministic taunt and quotes
    monkeypatch.setattr(game.random, "choice", lambda seq: seq[0])

    game.main()
    out = capsys.readouterr().out

    # Verify a full cycle happened and final score is correct
    assert "YOU CHOSE: SPOCK" in out
    assert "COMPUTER CHOSE: SCISSORS" in out
    assert "SPOCK SMASHES SCISSORS" in out or "YOU WIN" in out
    assert "SCORE: Wins: 1 | Losses: 0 | Ties: 0" in out
    assert "FINAL SCORE: Wins: 1 | Losses: 0 | Ties: 0" in out
    assert "Live long and prosper" in out or "Farewell" in out


def test_invalid_selection_in_main_then_valid(monkeypatch, capsys, reset_delay):
    # Sequence: invalid input 'x', then '0' (Rock), play again 'n'
    inputs = iter(["x", "0", "n"])
    monkeypatch.setattr(builtins, "input", lambda _prompt="": next(inputs))
    # Force computer to Rock as well to get a tie
    monkeypatch.setattr(game.random, "randint", lambda a, b: 0)
    monkeypatch.setattr(game.random, "choice", lambda seq: seq[0])

    game.main()
    out = capsys.readouterr().out
    assert "Invalid selection" in out
    assert "It's a tie" in out or "TIE" in out
    assert "SCORE: Wins: 0 | Losses: 0 | Ties: 1" in out
    assert "FINAL SCORE: Wins: 0 | Losses: 0 | Ties: 1" in out