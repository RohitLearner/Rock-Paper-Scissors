# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter

# TRY 4 (BEST ONE)
prev_work = {}
def player(prev_play, opponent_history=[]):
  global prev_work
  n = 3 #### Keep finding the optimal value.
  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "S" # default, until statistic kicks in

  if len(opponent_history)>n:
    inp = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in prev_work.keys():
      prev_work["".join(opponent_history[-(n+1):])]+=1
    else:
      prev_work["".join(opponent_history[-(n+1):])]=1

    possible =[inp+"R", inp+"P", inp+"S"]

    for i in possible:
      if not i in prev_work.keys():
        prev_work[i] = 0

    predict = max(possible, key=lambda key: prev_work[key])

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
TRY 4
 python3 main.py
Final results: {'p1': 996, 'p2': 1, 'tie': 3}
Player 1 win rate: 99.89969909729187%
Final results: {'p1': 481, 'p2': 277, 'tie': 242}
Player 1 win rate: 63.45646437994723%
Final results: {'p1': 413, 'p2': 263, 'tie': 324}
Player 1 win rate: 61.094674556213015%
Final results: {'p1': 750, 'p2': 209, 'tie': 41}
Player 1 win rate: 78.20646506777894%

 python3 test_module.py 

Testing game against abbey...
Final results: {'p1': 481, 'p2': 288, 'tie': 231}
Player 1 win rate: 62.54876462938882%
.Testing game against kris...
Final results: {'p1': 649, 'p2': 45, 'tie': 306}
Player 1 win rate: 93.51585014409221%
.Testing game against mrugesh...
Final results: {'p1': 824, 'p2': 174, 'tie': 2}
Player 1 win rate: 82.56513026052104%
.Testing game against quincy...
Final results: {'p1': 946, 'p2': 16, 'tie': 38}
Player 1 win rate: 98.33679833679834%
.
----------------------------------------------------------------------
Ran 4 tests in 0.085s

TRY 3 
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

Try 2
def player(prev_play,my_history = []):
    winning_set = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }
    if len(my_history)>1:
      if (winning_set[my_history[-1]]==prev_play):
        guess = winning_set[prev_play]
      else:
        guess = winning_set[my_history[-1]]
    else:
      guess = "P"
    my_history.append(guess)
    return guess

 python3 main.py
Final results: {'p1': 601, 'p2': 199, 'tie': 200}
Player 1 win rate: 75.125%
Final results: {'p1': 195, 'p2': 507, 'tie': 298}
Player 1 win rate: 27.77777777777778%
Final results: {'p1': 1, 'p2': 0, 'tie': 999}
Player 1 win rate: 100.0%
Final results: {'p1': 3, 'p2': 1, 'tie': 996}
Player 1 win rate: 75.0%
 python test_module.py 

Testing game against abbey...
Final results: {'p1': 173, 'p2': 505, 'tie': 322}
Player 1 win rate: 25.51622418879056%
FTesting game against kris...
Final results: {'p1': 1, 'p2': 0, 'tie': 999}
Player 1 win rate: 100.0%
.Testing game against mrugesh...
Final results: {'p1': 417, 'p2': 251, 'tie': 332}
Player 1 win rate: 62.4251497005988%
.Testing game against quincy...
Final results: {'p1': 600, 'p2': 199, 'tie': 201}
Player 1 win rate: 75.09386733416771%

'''
'''
Try 1
import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    numberList = ["R","P","S"]
    guess = "P"
    if len(opponent_history) > 2:
        guess = random.choice(numberList)
    if len(opponent_history) == 100:
      print(opponent_history)
    return guess
Output:
 python3 main.py 
Final results: {'p1': 335, 'p2': 323, 'tie': 342}
Player 1 win rate: 50.911854103343465%
Final results: {'p1': 336, 'p2': 353, 'tie': 311}
Player 1 win rate: 48.76632801161103%
Final results: {'p1': 356, 'p2': 326, 'tie': 318}
Player 1 win rate: 52.19941348973607%
Final results: {'p1': 335, 'p2': 353, 'tie': 312}
Player 1 win rate: 48.69186046511628%
 

'''