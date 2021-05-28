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
        
        
        
    def validate(self, dice_roll):
        validating = True
        while validating:
            user_input = input('> ').replace(' ', '')
            if user_input == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                sys.exit()
            is_valid = GameLogic.validate_keepers(dice_roll, list(user_input.replace(' ', '')))
            if is_valid and (user_input != ''):
                validating = False
                return user_input
            else:
                print('Cheater!!! Or possibly made a typo...')
                while not is_valid:
                    print(self.print_roll(dice_roll))
                    print('Enter dice to keep, or (q)uit:')
                    user_input = input('> ')
                    is_valid = GameLogic.validate_keepers(dice_roll, list(user_input.replace(' ', '')))
                    if is_valid:
                        return user_input.replace(' ', '')

    def hot_dice(self, dice_roll):
        dice_count = 0
        score = GameLogic.calculate_score(dice_roll)
        self.banker.shelf(score)
        print(f'You have {self.banker.shelved} unbanked points and {dice_count} dice remaining') 
        
    def play_round(self):
        dice_count = 6
        print(f'Starting round {self.round_num}')
        rolling = True
        while rolling and (dice_count > 0):
            print(f'Rolling {dice_count} dice...')
            dice_roll = list(self.roller(dice_count))
            print(self.print_roll(dice_roll))
            score = GameLogic.calculate_score(dice_roll)
            if score == 0:
                print('****************************************')
                print('**        Zilch!!! Round over         **')
                print('****************************************')
                print(f'You banked 0 points in round {self.round_num}')
                print(f'Total score is {self.banker.balance} points')
                return
                    
            print('Enter dice to keep, or (q)uit:')
            user_input = self.validate(dice_roll)
            scoring_dice = GameLogic.get_scorers(dice_roll)
                    
            if (scoring_dice == 'three pair') or (scoring_dice == 'straight') or (scoring_dice == 'six of a kind'):
                self.hot_dice(dice_roll)
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ')
                
                if user_input == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    sys.exit()
                
                if user_input == 'r':
                    continue
                
                if user_input == 'b':
                    rolling = False
                    banked = self.banker.bank()
                    print(f'You banked {banked} points in round {self.round_num}')
                    print(f'Total score is {self.banker.balance} points')
                    return

            if user_input.replace(' ', '').isnumeric():
                score = GameLogic.calculate_score(list(user_input))
                self.banker.shelf(score)
                for die in dice_roll:
                    if str(die) in user_input:
                        dice_count -= 1
                print(f'You have {self.banker.shelved} unbanked points and {dice_count} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ')
                if user_input == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    sys.exit()
                
                if user_input == 'r':
                    continue
                
                if user_input == 'b':
                    rolling = False
                    banked = self.banker.bank()
                    print(f'You banked {banked} points in round {self.round_num}')
                    print(f'Total score is {self.banker.balance} points')
                    return

    def print_roll(self, roll):
        string_roll = ' '.join(map(str, roll))
        return f'*** {string_roll} ***'


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
            while (self.round_num <= self.num_rounds):                
                self.play_round()  
                self.round_num += 1
            print(f'Thanks for playing. You earned {self.banker.balance} points')

if __name__ == "__main__":
    game = Game()
    game.play()    
                
                
                