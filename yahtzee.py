import os
import random
import re
import sys

from hand import Hand
from scoreboard import ScoreBoard
from yahtzee_rules import *


class YahtzeeGame:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
            YAHTZEE

            Welcome to the game. To begin, simply press [Enter]
            and follow the instructions on the screen.

            To exit, press [Ctrl+C]
            """)

        # Begin by instantiating the hand and scoreboard.
        self.hand = Hand()
        self.scoreboard = ScoreBoard()

        # Defining the rules of the game
        # Register the game rules
        self.scoreboard.register_rules([
            Aces(),
            Twos(),
            Threes(),
            Fours(),
            Fives(),
            Sixes(),
            ThreeOfAKind(),
            FourOfAKind(),
            FullHouse(),
            SmallStraight(),
            LargeStraight(),
            Yahtzee(),
            FibonYahtzee(),
            Chance(),
        ])

    def show_scoreboard_points(self, hand: Hand = None):
        print("\nSCOREBOARD")
        print("===================================")
        print(self.scoreboard.create_points_overview(hand))
        print("===================================")

    # Defining a method for which dices select to re-roll.
    def choose_dice_reroll(self):
        while True:
            try:
                reroll = input("\nChoose which dice to re-roll "
                               "(comma-separated or 'all', or 0 to continue:")

                if reroll.lower() == 'all':
                    return self.hand.all_dice()
                else:
                    # Perform some clean-up of input3 4
                    reroll = reroll.replace(" ", "")  # Remove Spaces
                    reroll = re.sub('[^0-9]', '', reroll)  # Remove non-numerals
                    reroll = reroll.split(",")  # Turn String into list
                    reroll = list(map(int, reroll))  # Turn strings in list to int

                if not reroll or 0 in reroll:
                    return []
                else:
                    return reroll

            except ValueError:
                print("You entered something other than a number")
                print("Please Try again")

    # Defining a method for select the scoring.
    def select_scoring(self):
        self.show_scoreboard_points(self.hand)
        while True:
            scoreboard_row_int = input("Choose which scoring to use: ")
            try:
                scoreboard_row_int = int(re.sub('[^0-9]', '', scoreboard_row_int))
                if scoreboard_row_int < 1 or scoreboard_row_int > self.scoreboard.rules_count():
                    print("Please select an existing scoring rule.")
                else:
                    return self.scoreboard.get_rule(scoreboard_row_int - 1)
            except ValueError:
                print("You entered something other than a number. PLease try again.")

    # Defining a method for each turn.
    def do_turn(self):
        # Now the turn is defined as a roll of the dice
        rolls = 0
        # Starting from all dices. Using the convenience method created in the hand class.
        selected_dice = self.hand.all_dice()
        while True:
            print("\nRolling Dice...")
            self.hand.roll(selected_dice)
            print(self.hand)
            rolls += 1

            # if we reached the max number of rolls, game over.
            if rolls >= 3:
                break

            # Choose which dice to reroll.
            selected_dice = self.choose_dice_reroll()
            if len(selected_dice) == 0:
                break

        rule = self.select_scoring()

        points = self.scoreboard.assign_points(rule, self.hand)
        print(f"Adding {points} points to {rule.name()}")
        self.show_scoreboard_points()

        input("\nPress any key to continue")
        os.system('cls' if os.name == 'nt' else 'clear')

    # Defining the overall game progression
    def play(self):
        # The game will keep going until the board is full.
        for _ in range(self.scoreboard.rules_count()):
            self.do_turn()

        print("\nCongratulations,! You finished the game!\n")
        self.show_scoreboard_points()
        print(f"Total points: {self.scoreboard.total_points()}")


if __name__ == '__main__':
    try:
        game = YahtzeeGame()
        game.play()
    except KeyboardInterrupt:
        print("\nExiting...")
