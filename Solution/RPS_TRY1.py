# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter
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
'''
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

Testing game against abbey...
Final results: {'p1': 347, 'p2': 314, 'tie': 339}
Player 1 win rate: 52.49621785173979%
FTesting game against kris...
Final results: {'p1': 317, 'p2': 326, 'tie': 357}
Player 1 win rate: 49.30015552099534%
FTesting game against mrugesh...
Final results: {'p1': 328, 'p2': 329, 'tie': 343}
Player 1 win rate: 49.923896499238964%
FTesting game against quincy...
Final results: {'p1': 329, 'p2': 332, 'tie': 339}
Player 1 win rate: 49.77307110438729%
'''
