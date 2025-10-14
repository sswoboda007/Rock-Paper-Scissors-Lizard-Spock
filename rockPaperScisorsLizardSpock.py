# -*- coding: utf-8 -*-
# Rock-Paper-Scissors-Lizard-Spock/rockPaperScisorsLizardSpock.py
"""A script to play Rock-Paper-Scissors-Lizard-Spock against the computer.

This script implements the game logic for Rock-Paper-Scissors-Lizard-Spock,
a variant of the classic game. The user is prompted to make a choice, and the
computer makes a random selection. The winner is then determined and displayed.
The user can choose to play again or exit the game.

Author: @seanl
Version: 1.0.0
Creation Date: 10/24/2021
Last Updated: 10/13/2025
"""

import random
import time
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4
delayA = float(1.0)

victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def countDown():
    """Prints a countdown sequence to build suspense before revealing results."""
    print("**Rock**")
    time.sleep(delayA)
    print("**Paper**")
    time.sleep(delayA)
    print("**Scisors**")
    time.sleep(delayA)
    print("**Lizard**")
    time.sleep(delayA)
    print("**Spock**")
    time.sleep(delayA)
    print("Shoot...")
    time.sleep(delayA)
         
def getUserSelection():
    """Prompts the user for their action and returns it.

    Returns:
        Action: The user's selected action as an Action enum member.

    """
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choicesStr = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choicesStr}): "))
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
    """Determines and prints the winner of the round.

    Args:
        userAction (Action): The action selected by the user.
        computerAction (Action): The action selected by the computer.

    """
    defeats = victories[userAction]
    if userAction == computerAction:
        print(f"Both players selected {userAction.name}. It's a tie!")
    elif computerAction in defeats:
        print(f"{userAction.name} beats {computerAction.name}! You win!")
    else:
        print(f"{computerAction.name} beats {userAction.name}! You lose.")

while True:
    try:
        userAction = getUserSelection()
    except ValueError as e:
        rangeStr = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {rangeStr}")
        continue

    computerAction = getComputerSelection()
    countDown() 
    determineWinner(userAction, computerAction)

    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break