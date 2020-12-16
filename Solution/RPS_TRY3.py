# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter

wtf = {}
def player(prev_play, opponent_history=[]):
  global wtf
  n = 5
  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R" # default, until statistic kicks in

  if len(opponent_history)>n:
    inp = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in wtf.keys():
      wtf["".join(opponent_history[-(n+1):])]+=1
    else:
      wtf["".join(opponent_history[-(n+1):])]=1

    possible =[inp+"R", inp+"P", inp+"S"]

    for i in possible:
      if not i in wtf.keys():
        wtf[i] = 0

    predict = max(possible, key=lambda key: wtf[key])

    if predict[-1] == "P":
      numberList = ["S"]
      guess = random.choice(numberList)
    if predict[-1] == "R":
      numberList = ["P"]
      guess = random.choice(numberList)
    if predict[-1] == "S":
      numberList = ["R"]
      guess = random.choice(numberList)
  return guess
'''
 python main.py
Final results: {'p1': 992, 'p2': 3, 'tie': 5}
Player 1 win rate: 99.69849246231156%
Final results: {'p1': 443, 'p2': 315, 'tie': 242}
Player 1 win rate: 58.443271767810025%
Final results: {'p1': 644, 'p2': 209, 'tie': 147}
Player 1 win rate: 75.49824150058618%
Final results: {'p1': 825, 'p2': 159, 'tie': 16}
Player 1 win rate: 83.84146341463415%
 python test_module.py 

Testing game against abbey...
Final results: {'p1': 422, 'p2': 319, 'tie': 259}
Player 1 win rate: 56.95006747638327%
FTesting game against kris...
Final results: {'p1': 865, 'p2': 51, 'tie': 84}
Player 1 win rate: 94.43231441048034%
.Testing game against mrugesh...
Final results: {'p1': 822, 'p2': 169, 'tie': 9}
Player 1 win rate: 82.9465186680121%
.Testing game against quincy...
Final results: {'p1': 992, 'p2': 3, 'tie': 5}
Player 1 win rate: 99.69849246231156%  
'''
