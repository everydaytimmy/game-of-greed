from game_of_greed.game_logic import GameLogic
from game_of_greed.game_functions import Game_functions

class Game(Game_functions):
    """Class for Game of Greed application.
    Inherits functionality from Game_functions class. 
    """

    def play_round(self):
        """a series of steps that dictate what happens during one round of gameplay.
        Return indicates the round is over, continue indicates to roll the dice again.
        """
        self.dice_count = 6
        print(f'Starting round {self.round_num}')
        
        while self.dice_count > 0:
            dice_roll = self.roll_the_dice()
            score = GameLogic.calculate_score(dice_roll)
            if score == 0:
                self.print_zilcher()
                return
                    
            print('Enter dice to keep, or (q)uit:')
            user_input = self.validate_user_input(dice_roll)
            roll_is_special = GameLogic.check_for_special_roll(dice_roll)
            
            if roll_is_special:
                self.hot_dice(dice_roll)
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ')
                
                if user_input == 'q':
                    self.quit_game()
                
                if user_input == 'r':
                    continue
                
                if user_input == 'b':
                    self.bank_points()
                    return

            if user_input.isnumeric():
                self.shelve_points_and_adjust_dice_count(dice_roll, user_input)
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ')
                
                if user_input == 'q':
                    self.quit_game()
                
                if user_input == 'r':
                    continue
                
                if user_input == 'b':
                    self.bank_points()
                    return

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
                
                
                