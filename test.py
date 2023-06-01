# Rock, paper, scissors

import random
import os 
import re

os.system('cls' if os.name == 'nt'else 'clear')

while(1 < 2):
    print("\n")
    print("Rock, Paper, Scissors -shoot!")
    
userChoice = input("choose your weapon [R]ock, [P]aper, [S]cissors: ")

if not re.match("[SsRrPp]", userChoice):
    print("choose weapon:")    
    print("[R]ock, [P]aper, [S]cissors ")
    continue
# echo user's choice

print("your choice: " + userChoice)
choices = ['R', 'P', 'S']

opponentChoice = random.choice(choices)

print("I chose:" + opponentChoice)

if opponentChoice == str.upper(userChoice):
    print("tie !")
    
#opponent choice == str 'R' and str.upper()== 'P'

elif opponentChoice == 'R' and userChoice.upper() == 'S':
    print("Rock beats scissors, i win!")
    continue  

elif opponentChoice == 'S' and userChoice.upper() == 'P':
    print("Scissors beats paper, i win!")
    continue

elif opponentChoice == 'P' and userChoice.upper() == 'R':
    print("Paper beats rock, i win!")
    continue

else:
    print("You win!")
    
    
    
