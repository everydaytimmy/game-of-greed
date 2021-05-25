import sys
from typing import NoReturn

from game_of_greed.game_logic import GameLogic, Banker

class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
        self.roller = None


    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')
        play_game = input("> ")
        if play_game == 'n':
            print('OK. Maybe another time')
        
        if play_game == 'y':
            self.round_num += 1
            while self.round_num <= self.num_rounds:
                dice_count = 6
                print(f'Starting round {self.round_num}')
                print(f'Rolling 6 dice...')
                dice_roll = self.roller(dice_count)
                (a, b, c, d, e, f) = dice_roll
                print(f'*** {a} {b} {c} {d} {e} {f} ***')
                print('Enter dice to keep, or (q)uit:')
                user_input = input('> ')
                if user_input == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    break
                score = GameLogic.calculate_score(dice_roll)
                self.banker.shelf(score)
                for die in dice_roll:
                    if int(user_input) == die:
                        dice_count -= 1
                print(f'You have {self.banker.shelved} unbanked points and {dice_count} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ')
                if user_input == 'q':
                    print('Thanks for playing. You earned {self.banker.balance} points')
                    break
                if user_input == 'b':
                    banked = self.banker.bank()
                    print(f'You banked {banked} points in round {self.round_num}')
                    print(f'Total score is {self.banker.balance} points')
                if user_input == 'r':
                    dice_roll = self.roller(dice_count)
                self.round_num += 1

                    
                
                
                