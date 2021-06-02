import sys
from game_of_greed.game_logic import GameLogic, Banker

class Game_functions:
    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
        self.dice_count = 6
        self.roller = None
        
    def bank_points(self):
        """
        Bank shelved points and print message for user updating them on the gamestate
        """
        banked = self.banker.bank()
        print(f'You banked {banked} points in round {self.round_num}')
        print(f'Total score is {self.banker.balance} points')
        
    def quit_game(self):
        """
        Prints exit message for user and exits the game.
        """
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()
        
    def validate_user_input(self, dice_roll):
        """this method takes in the dice roll and makes sure the user is selecting dice to keep that
        actually match the options that are available to keep.

        Args:
            dice_roll (list): a list of dice that were rolled

        Returns:
            [string]: returns the validated user input of dice to keep from a roll.
        """

        user_input = input('> ').replace(' ', '')
        if user_input == 'q':
            self.quit_game()
        
        is_valid = GameLogic.validate_keepers(dice_roll, list(user_input))
        if is_valid:
            return user_input
        
        print('Cheater!!! Or possibly made a typo...')
        while not is_valid:
            self.print_roll(dice_roll)
            print('Enter dice to keep, or (q)uit:')
            user_input = input('> ').replace(' ', '')
            is_valid = GameLogic.validate_keepers(dice_roll, list(user_input))
            if is_valid:
                return user_input
        
    def print_roll(self, roll):
        """Prints the dice that were rolled

        Args:
            roll (list): roll is the dice that were rolled by the roller

        Returns:
            [string]: returns the formatted string to be printed
        """
        string_roll = ' '.join(map(str, roll))
        print(f'*** {string_roll} ***')
        
    def calculate_remaining_dice(self, dice_roll, user_input):
        """Adjusts the number of dice available for the next roll.

        Args:
            dice_roll (list): a list of dice that were rolled. values of 1-6.
            user_input (string): a string of numbers representing that the user has decided to keep.
        """
        for die in dice_roll:
            if str(die) in user_input:
                self.dice_count -= 1
    
    def print_zilcher(self):
        """
        Prints a message to the user if the previous roll has no scoring dice.
        """
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {self.round_num}')
        print(f'Total score is {self.banker.balance} points')
        self.banker.clear_shelf()
        
    def roll_the_dice(self):
        """Rolls dice available and prints a message to the user showing them what was rolled.

        Returns:
            [list]: a list containing the values of each die that was rolled. Numbers are 1-6.
        """
        print(f'Rolling {self.dice_count} dice...')
        dice_roll = list(self.roller(self.dice_count))
        self.print_roll(dice_roll)
        return dice_roll
        
    def shelve_points_and_adjust_dice_count(self, dice_roll, user_input):
        """Calculates the score value of dice that the user has decided to keep, shelves the score, and calculates the remaining dice.

        Args:
            dice_roll (list): a list of numbers ranging from 1-6
            user_input (string): a string of numbers represnting the dice the user has decided to keep
        """
        score = GameLogic.calculate_score(list(user_input))
        self.banker.shelf(score)
        self.calculate_remaining_dice(dice_roll, user_input)
        print(f'You have {self.banker.shelved} unbanked points and {self.dice_count} dice remaining')
        
    