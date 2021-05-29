import pytest, re
from tests.flo import diff
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


def test_what_gets_shelved():
  """The shelved points should be equal to the score of the dice the user chooses to keep,
  not the score of the entire roll.
  """
  diffs = diff(Game().play, path="tests/version_5/what_gets_shelved.txt")
  
  assert not diffs, diffs