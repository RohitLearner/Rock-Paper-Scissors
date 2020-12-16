# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter

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
'''
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
