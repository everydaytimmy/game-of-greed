import random

scoresheet = {
  '1': {'1': 100, '2': 200, '3': 1000, '4': 2000, '5': 3000, '6': 4000},
  '2': {'1': 0, '2': 0, '3': 200, '4': 400, '5': 600, '6': 800},
  '3': {'1': 0, '2': 0, '3': 300, '4': 600, '5': 900, '6': 1200},
  '4': {'1': 0, '2': 0, '3': 400, '4': 800,'5': 1200, '6': 1600},
  '5': {'1': 50, '2': 100, '3': 500, '4': 1000,'5': 1500, '6': 2000},
  '6': {'1': 0, '2': 0, '3': 600, '4': 1200,'5': 1800, '6': 2400},
  'special': {'straight': 1500, 'three pair': 1500}
}

class Banker:
  """the Banker class will handle the organization of points during gameplay
  """
  def __init__(self):
    self.balance = 0
    self.shelved = 0

  def shelf(self, num):
    """the shelf method takes a score and sets it aside on the shelf for further processing.

    Args:
        num (int): the score to be shelved.
    """
    self.shelved += num

  def bank(self):
    """takes points from the shelf and puts them in the bank.

    Returns:
        [int]: returns the points that were taken from the shelf and put into the bank.
    """
    deposit = self.shelved
    self.balance += deposit
    self.shelved = 0
    return deposit

  def clear_shelf(self):
    """takes points that were on the shelf and gets rid of them.

    Returns:
        [int]: returns 0 to indicate that the shelf has been cleared of points.
    """
    self.shelved = 0
    return self.shelved
  
  
  

class GameLogic:
  """this class handles the scoring logic and logic related to scoring.
  """

  def roll_dice(num_dice):
    """generates a random number between 1 and 6 for a given number of dice.

    Args:
        dice (int): the number of dice to be rolled.

    Returns:
        [list]: returns the simulated rolls for the given number of dice.
    """
    return [random.randint(1,6) for _ in range(0, num_dice)]

  @staticmethod
  def calculate_score(dice):
    """calculates the score of a given dice roll according to the scoresheet.

    Args:
        dice (tuple): a tuple representing the dice that were rolled.

    Returns:
        [int]: returns the calculated score of a dice roll.
    """
    occurrences = {num: dice.count(num) for num in dice}

    # first, check for special cases
    if sorted(dice) == [1,2,3,4,5,6]:
      return scoresheet['special']['straight']

    keys = list(occurrences.keys())
    if len(occurrences) == 3:
      if (occurrences[keys[0]] == 2) and (occurrences[keys[1]] == 2) and (occurrences[keys[2]] == 2):
        return scoresheet['special']['three pair']

    # then check for regular scores
    return sum([scoresheet[str(num)][str(occurrences[num])] for num in occurrences])

  @staticmethod
  def get_scorers(dice):
    """determines which dice score, and if the scoring dice are a special category of roll.

    Args:
        dice (list): the face value of the dice that were rolled.

    Returns:
        [tuple, string]: by default returns a tuple of numbers representing the dice that do score,
        and returns a string if the scoring dice are a special category of roll.
    """
    occurrences = {num: dice.count(num) for num in dice}
      
    scoring_dice = [num for num in occurrences if scoresheet[str(num)][str(occurrences[num])]]

    keys = list(occurrences.keys())
    if isinstance(keys, list):
      if len(keys) == 3:
        if (occurrences[keys[0]] == 2) and (occurrences[keys[1]] == 2) and (occurrences[keys[2]] == 2):
          return 'three pair'

    if (isinstance(keys, int)) and (len(occurrences[str(keys)]) == 6):
      return 'six of a kind'
      
    return scoring_dice

  @staticmethod
  def validate_keepers(roll, keepers):
    """makes sure that the user is not trying to keep more dice than are available to keep

    Args:
        roll (list): a list of dice values that were rolled
        keepers (string): a string containing dice values that the user wants to keep

    Returns:
        [boolean]: returns True if the user has requested to keep a valid number of dice, and False if they have
        requested to keep dice that do not exist
    """
    
    for num in keepers:
      if num:
        if keepers.count(num) > roll.count(int(num)):
          return False

    return True

  @staticmethod
  def check_for_special_roll(dice):
    occurrences = {num: dice.count(num) for num in dice}
    
    keys = list(occurrences.keys())
    if isinstance(keys, list):
      if len(keys) == 3:
        if (occurrences[keys[0]] == 2) and (occurrences[keys[1]] == 2) and (occurrences[keys[2]] == 2):
          return 'three pair'

    if (isinstance(keys, int)) and (len(occurrences[str(keys)]) == 6):
      return 'six of a kind'