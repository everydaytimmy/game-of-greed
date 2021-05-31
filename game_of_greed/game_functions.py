import sys
from game_of_greed.game_logic import GameLogic, Banker

class Game_functions:
    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
        self.roller = None
        
    def bank_points(self):
        banked = self.banker.bank()
        print(f'You banked {banked} points in round {self.round_num}')
        print(f'Total score is {self.banker.balance} points')
        
    def quit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()
        
    def validate_user_input(self, dice_roll):
        """this method takes in the dice roll and makes sure the user is putting in numbers to keep that that
        actually match the options that are available to keep.

        Args:
            dice_roll ([list]): a list of dice that were rolled

        Returns:
            [string]: returns the validated user input of dice to keep from a roll.
        """

        user_input = input('> ').replace(' ', '')
        if user_input == 'q':
            print(f'Thanks for playing. You earned {self.banker.balance} points')
            sys.exit()
            
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

    def hot_dice(self, dice_roll):
        """ if the dice roll is either 3 pair, a straight, or six of a kind, that means the user has hot dice and
        gets to choose if they want to reroll with 6 fresh dice, or bank the points they just got. the points are automatically shelved.

        Args:
            dice_roll ([list]): dice roll is the face number of each die that was rolled
        """
        dice_count = 0
        score = GameLogic.calculate_score(dice_roll)
        self.banker.shelf(score)
        print(f'You have {self.banker.shelved} unbanked points and {dice_count} dice remaining') 
        
    def print_roll(self, roll):
        """Prints the dice that were rolled

        Args:
            roll ([list]): roll is the dice that were rolled by the roller

        Returns:
            [string]: returns the formatted string to be printed
        """
        string_roll = ' '.join(map(str, roll))
        print(f'*** {string_roll} ***')
        
    def calculate_remaining_dice(self, dice_roll, user_input, dice_count):
      for die in dice_roll:
          if str(die) in user_input:
              dice_count -= 1
      return dice_count
    
    def print_zilcher(self):
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {self.round_num}')
        print(f'Total score is {self.banker.balance} points')
        
    def roll_dice(self, dice_count):
        print(f'Rolling {dice_count} dice...')
        dice_roll = list(self.roller(dice_count))
        self.print_roll(dice_roll)
        return dice_roll, dice_count
      
    def shelve_points_and_adjust_dice_count(self, dice_roll, user_input, dice_count):
        score = GameLogic.calculate_score(list(user_input))
        self.banker.shelf(score)
        dice_count = self.calculate_remaining_dice(dice_roll, user_input, dice_count)
        print(f'You have {self.banker.shelved} unbanked points and {dice_count} dice remaining')
        return dice_count