# -*- coding: utf-8 -*-
# Rock-Paper-Scissors-Lizard-Spock/ascii_images.py
"""ASCII Art collection for Rock-Paper-Scissors-Lizard-Spock game.

This module contains all the awesome ASCII art used in the game,
including action representations and epic battle scenes!

Author: @seanl
Version: 1.0.0
Creation Date: 10/13/2025
"""


class AsciiArt:
    """Collection of ASCII art for the game."""

    GAME_TITLE = r"""
    ╦═╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╦╔═╗╔═╗╔═╗╦═╗╔═╗  ╦  ╦╔═╗╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔═╗╔═╗╦╔═
    ╠╦╝║ ║║  ╠╩╗  ╠═╝╠═╣╠═╝║╣ ╠╦╝  ╚═╗║  ║╚═╗╚═╗║ ║╠╦╝╚═╗  ║  ║╔═╝╠═╣╠╦╝ ║║  ╚═╗╠═╝║ ║║  ╠╩╗
    ╩╚═╚═╝╚═╝╩ ╩  ╩  ╩ ╩╩  ╚═╝╩╚═  ╚═╝╚═╝╩╚═╝╚═╝╚═╝╩╚═╚═╝  ╩═╝╩╚═╝╩ ╩╩╚══╩╝  ╚═╝╩  ╚═╝╚═╝╩ ╩
    """

    ROCK = r"""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

    PAPER = r"""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

    SCISSORS = r"""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

    LIZARD = r"""
              _,--._.-,
             /\_r-,\_ )
        .-.) _;='_/ (.;
         \ \'     \/S )
          L.'-. _.'|-'
         <_`-'\'_.'/
           `'-._( \
            ___   \\,      ___
           \ .'-. \\   .-'_. /
            '._' '.\\/.-'_.'
               '--``\('--'
                  \\  \\
                  `\\  \\
                    \\  \\
                     \\_\\
    """

    SPOCK = r"""
           _  _
          | \/ |
          |    |    Live Long
          | /\ |    & Prosper!
          |_||_|
            ||
           /||\
          / || \
         /  ||  \
            /\
           /  \
          /    \
    """

    # Epic Battle Scenes!
    BATTLE_SCENES = {
        # Spock vaporizes Rock
        (4, 0): r"""
        ⚡ SPOCK VAPORIZES ROCK! ⚡

           🖖              💥
          /||\     ~~~~~~>  ___
         / || \    ~~~>    (   )
        /  ||  \   ~~>      \_/
                   ~>        *
                  VAPORIZED!
        """,

        # Rock crushes Scissors
        (0, 2): r"""
        💥 ROCK CRUSHES SCISSORS! 💥

            ___
           (   )
            \_/      ✂️
             |   💥  /\
             |  CRUSH \/
            / \      XX
        """,

        # Scissors cuts Paper
        (2, 1): r"""
        ✂️ SCISSORS CUTS PAPER! ✂️

           ✂️
           /\      📄
          /  \    /|
         /SNIP\  / |
        /_____\ |~~|
                |  |
               SHRED!
        """,

        # Paper covers Rock
        (1, 0): r"""
        📄 PAPER COVERS ROCK! 📄

          ________
         /        \
        |  PAPER   |
        |   📄    |___
        |        (   )
         \_______ \_/
           COVERED!
        """,

        # Rock crushes Lizard
        (0, 3): r"""
        💥 ROCK CRUSHES LIZARD! 💥

            ___
           (   )
            \_/
             |    🦎
             |   SQUISH!
            / \    XX
        """,

        # Lizard poisons Spock
        (3, 4): r"""
        🦎 LIZARD POISONS SPOCK! 🦎

           🦎
          /|~     🖖
         / |~~>  /||\  
        /  |~~~>/ || \  💀
           BITE! ||
                /||\
        """,

        # Spock smashes Scissors
        (4, 2): r"""
        🖖 SPOCK SMASHES SCISSORS! 🖖

           🖖
          /||\    ✂️
         / || \  /  \
        /  ||  \/ SMASH!
           ||    \___/
          KARATE   XX
           CHOP!
        """,

        # Scissors decapitates Lizard
        (2, 3): r"""
        ✂️ SCISSORS DECAPITATES LIZARD! ✂️

           ✂️
           /\     🦎
          /  \   /|
         / SNIP\ ||
        /_______\||
                HEAD OFF!
        """,

        # Lizard eats Paper
        (3, 1): r"""
        🦎 LIZARD EATS PAPER! 🦎

           🦎      📄
          /|~     /|
         / |CHOMP||
        /  |~~~>~||
           NOM    XX
           NOM!
        """,

        # Paper disproves Spock
        (1, 4): r"""
        📄 PAPER DISPROVES SPOCK! 📄

          ________
         /SCIENCE \
        |  PAPER   |  🖖
        |  PROVES  | /||\
        |   YOU    |/ || \
         \ WRONG! /  ||
          \______/  LOGIC
                   FAIL!
        """,
    }

    TIE_SCENE = r"""
        🤝 === TIE! === 🤝

          👤      👤
          /|\    /|\
          / \    / \

        SAME CHOICE!
    """

    GOODBYE_SCENE = r"""
        🖖 FAREWELL, HUMAN! 🖖

           _  _
          | \/ |
          |    |
          | /\ |
          |_||_|
            ||
           /||\
          / || \
         /  ||  \

        Thanks for playing!
    """


# Additional fun ASCII art that could be used for special occasions
class BonusArt:
    """Bonus ASCII art for special moments."""

    SHELDON = r"""
        BAZINGA!
         ___
        |   |
        | O |
        |___|
         /|\
        / | \
         / \
        /   \
    """

    TROPHY = r"""
        ___________
       '._==_==_=_.'
       .-\:      /-.
      | (|:.     |) |
       '-|:.     |-'
         \::.    /
          '::. .'
            ) (
          _.' '._
         `"""""""`
    """

    EXPLOSION = r"""
                    ____
              ,-'~~~~    ~.
            ,'              ~.
           |              ____|____
          |            ,'          `.
         |            /              \
        |            |                |
       |            |                  |
      |            |                    |
     |            |                      |
    |            |                        |
    |           |                          |
    |          |      💥 BOOM! 💥          |
    |         |                            |
     |       |                            |
      |     |                            |
       |   |                            |
        | |                            |
         |                            |
    """