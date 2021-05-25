import random


class GameLogic:


  def roll_dice(dice):
    total = []
    while dice > 0:
      roll = random.randint(1, 6)
      total.append(roll)
      dice -= 1
    return total

class Banker:
  def __init__(self):
    self.balance = 0
    self.shelved = 0
  def shelf(self, num):
    self.shelved += num
  def bank(self):
    deposit = self.shelved
    self.balance += deposit
    self.shelved = 0
    return deposit
  def clear_shelf(self):
    self.shelved = 0
    return self.shelved

class GameLogic:
  @staticmethod
  def calculate_score(score):
    counter = 0
    if score.count(5) == 3:
      counter += 500
    if score.count(1) == 3:
      counter += 1000
    if score.count(1) == 6:
      counter += 4000
    if score.count(2) > 2:
      pass
    if score.count(2) == 4:
      counter += 400
    if score.count(2) == 5:
      counter += 600
    if score.count(2) == 6:
      counter += 800
    if score.count(1) == 6:
      counter += 4000
    s = sorted(list(score))
    if s == [1,2,3,4,5,6]:
      counter += 1500
    for num in score:
      occurrence_of_num = score.count(num)
      if occurrence_of_num <= 2:
        for num in score:
          if (num == 5) and not(score.count(5) >= 3) and not(sorted(list(score)) == [1,2,3,4,5,6]):
            counter += num*10
          if (num == 1) and not(score.count(1) >= 3) and not(sorted(list(score)) == [1,2,3,4,5,6]) and not(score.count(1) == 6):
            counter += num * 100
      else:
        amount = num *100
        # for each occurrence about 3, add the amount
        for _ in range(3,occurrence_of_num):
          amount += num*100
        counter += amount
    return counter