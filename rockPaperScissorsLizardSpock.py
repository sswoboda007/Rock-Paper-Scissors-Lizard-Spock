# -*- coding: utf-8 -*-
# Rock-Paper-Scissors-Lizard-Spock/rockPaperScissorsLizardSpock.py
"""A script to play Rock-Paper-Scissors-Lizard-Spock against the computer.

This script implements the game logic for Rock-Paper-Scissors-Lizard-Spock,
as famously explained by Dr. Sheldon Cooper. Now with EPIC ASCII ART!

Author: @seanl (Enhanced with Big Bang Theory humor & ASCII Art)
Version: 3.0.0 - "The Visual Spectacular Edition"
Creation Date: 10/24/2021
Last Updated: 10/13/2025
"""

import random
import time
from enum import IntEnum
from ascii_images import AsciiArt  # Import our cool ASCII art module


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


delayA = float(1.0)

# The sacred rules as decreed by Sheldon Cooper
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

# Sheldon-approved victory explanations
victory_explanations = {
    (Action.Scissors, Action.Paper): "Scissors cuts paper",
    (Action.Paper, Action.Rock): "Paper covers rock",
    (Action.Rock, Action.Lizard): "Rock crushes lizard",
    (Action.Lizard, Action.Spock): "Lizard poisons Spock",
    (Action.Spock, Action.Scissors): "Spock smashes scissors",
    (Action.Scissors, Action.Lizard): "Scissors decapitates lizard",
    (Action.Lizard, Action.Paper): "Lizard eats paper",
    (Action.Paper, Action.Spock): "Paper disproves Spock",
    (Action.Spock, Action.Rock): "Spock vaporizes rock",
    (Action.Rock, Action.Scissors): "Rock crushes scissors"
}

# Snarky computer taunts (Sheldon-style)
computer_taunts = [
    "Bazinga! Prepare to be defeated!",
    "Your inferior neural pathways are no match for my algorithms!",
    "I'm not insane, my mother had me tested. Now let's play!",
    "In a world where logic prevails, you don't stand a chance!",
    "I'm about to defeat you with the power of SCIENCE!",
    "Prepare yourself for a lesson in game theory!",
]

# Victory celebrations
victory_quotes = [
    "🎉 Astonishing! You've achieved the statistically improbable!",
    "🎊 Well, well... even a broken clock is right twice a day.",
    "🏆 Impressive! You must have a higher IQ than I initially calculated.",
    "✨ Fascinating! Your victory defies my probability models!",
    "🌟 Remarkable! Did you study game theory at Caltech?",
]

# Defeat messages
defeat_quotes = [
    "💀 As expected. My superior intellect prevails once again!",
    "🤖 Bazinga! Another victory for artificial intelligence!",
    "😏 Perhaps you should stick to simpler games, like tic-tac-toe.",
    "🧠 The odds were never in your favor. Better luck next time, homo sapien!",
    "🎯 Predictable. I calculated that move three iterations ago!",
]

# Tie messages
tie_quotes = [
    "🤝 A tie? How... pedestrian. Great minds think alike, I suppose.",
    "😐 We're in a quantum superposition of winning and losing. How tedious.",
    "🔄 A stalemate. This is like watching two parallel lines trying to meet.",
    "⚖️ Perfectly balanced, as all things should be... wait, wrong franchise.",
]


def printBanner():
    """Prints an epic ASCII banner for the game."""
    print("\n" + "=" * 70)
    print(AsciiArt.GAME_TITLE)
    print("=" * 70)
    print("                    As seen on 'The Big Bang Theory'!")
    print("\nScissors cuts Paper. Paper covers Rock. Rock crushes Lizard.")
    print("Lizard poisons Spock. Spock smashes Scissors. Scissors decapitates")
    print("Lizard. Lizard eats Paper. Paper disproves Spock. Spock vaporizes")
    print("Rock. And as it always has, Rock crushes Scissors!")
    print("=" * 70 + "\n")


def showActionArt(action):
    """Display ASCII art for the given action.

    Args:
        action (Action): The action to display art for.
    """
    art_map = {
        Action.Rock: AsciiArt.ROCK,
        Action.Paper: AsciiArt.PAPER,
        Action.Scissors: AsciiArt.SCISSORS,
        Action.Lizard: AsciiArt.LIZARD,
        Action.Spock: AsciiArt.SPOCK
    }
    print(art_map.get(action, ""))


def showBattleScene(winner_action, loser_action):
    """Display an epic battle scene between two actions.

    Args:
        winner_action (Action): The winning action.
        loser_action (Action): The losing action.
    """
    battle_key = (winner_action, loser_action)
    battle_art = AsciiArt.BATTLE_SCENES.get(battle_key, "")
    if battle_art:
        print("\n" + "~" * 70)
        print(battle_art)
        print("~" * 70 + "\n")


def countDown():
    """Prints a countdown sequence to build suspense before revealing results."""
    countdown_items = ["**Rock**", "**Paper**", "**Scissors**", "**Lizard**", "**Spock**"]

    for item in countdown_items:
        print(item)
        time.sleep(delayA * 0.6)

    print("\n💥 SHOOT! 💥\n")
    time.sleep(delayA * 0.5)


def getUserSelection():
    """Prompts the user for their action and returns it.

    Returns:
        Action: The user's selected action as an Action enum member.
    """
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choicesStr = ", ".join(choices)
    print(f"\n🎮 {random.choice(computer_taunts)}")
    selection = int(input(f"\n👉 Enter your choice ({choicesStr}): "))
    action = Action(selection)
    return action


def getComputerSelection():
    """Generates a random action for the computer.

    Returns:
        Action: The computer's randomly selected action as an Action enum member.
    """
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determineWinner(userAction, computerAction):
    """Determines and prints the winner of the round with dramatic flair.

    Args:
        userAction (Action): The action selected by the user.
        computerAction (Action): The action selected by the computer.
    """
    print(f"\n{'═' * 70}")
    print(f"              🧑 YOU CHOSE: {userAction.name.upper()}")
    print(f"{'═' * 70}")
    showActionArt(userAction)

    time.sleep(delayA * 0.8)

    print(f"\n{'═' * 70}")
    print(f"           🤖 COMPUTER CHOSE: {computerAction.name.upper()}")
    print(f"{'═' * 70}")
    showActionArt(computerAction)

    time.sleep(delayA * 0.8)

    defeats = victories[userAction]

    if userAction == computerAction:
        print(f"\n{'─' * 70}")
        print(AsciiArt.TIE_SCENE)
        print(f"{random.choice(tie_quotes)}")
        print(f"Both players selected {userAction.name}. It's a tie!")
        print(f"{'─' * 70}\n")
    elif computerAction in defeats:
        explanation = victory_explanations.get((userAction, computerAction), "")
        showBattleScene(userAction, computerAction)
        print(f"{'─' * 70}")
        print(f"⚔️  {explanation.upper()}! ⚔️")
        print(f"{random.choice(victory_quotes)}")
        print(f"🎯 {userAction.name} beats {computerAction.name}! YOU WIN! 🎯")
        print(f"{'─' * 70}\n")
    else:
        explanation = victory_explanations.get((computerAction, userAction), "")
        showBattleScene(computerAction, userAction)
        print(f"{'─' * 70}")
        print(f"💥 {explanation.upper()}! 💥")
        print(f"{random.choice(defeat_quotes)}")
        print(f"😢 {computerAction.name} beats {userAction.name}! YOU LOSE! 😢")
        print(f"{'─' * 70}\n")


def main():
    """Main game loop with enhanced user experience."""
    printBanner()

    wins = 0
    losses = 0
    ties = 0

    while True:
        try:
            userAction = getUserSelection()
        except ValueError:
            rangeStr = f"[0, {len(Action) - 1}]"
            print(f"\n❌ Invalid selection! Enter a value in range {rangeStr}")
            print("Even Penny knows how to follow simple instructions! 🙄\n")
            continue

        computerAction = getComputerSelection()
        countDown()

        determineWinner(userAction, computerAction)

        # Update score
        defeats = victories[userAction]
        if userAction == computerAction:
            ties += 1
        elif computerAction in defeats:
            wins += 1
        else:
            losses += 1

        # Display score
        print(f"📊 SCORE: Wins: {wins} | Losses: {losses} | Ties: {ties}\n")

        playAgain = input("🔄 Play again? (y/n): ")
        if playAgain.lower() != "y":
            print("\n" + "=" * 70)
            print(AsciiArt.GOODBYE_SCENE)
            print(f"🏁 FINAL SCORE: Wins: {wins} | Losses: {losses} | Ties: {ties}")
            if wins > losses:
                print("👑 Congratulations! You've proven yourself worthy!")
            elif wins < losses:
                print("🤓 Better luck next time! Perhaps more practice is needed.")
            else:
                print("🤝 A perfect balance. How... logical.")
            print("🖖 Live long and prosper! (Or at least until the next game)")
            print("=" * 70 + "\n")
            break
        print("\n" + "─" * 70 + "\n")


if __name__ == "__main__":
    main()