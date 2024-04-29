import random
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    
# Scores initial values
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] # A list
clear_terminal()
while True:
    
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        clear_terminal()
        print("Type something!")
        continue

    random_number = random.randint(0, 2) # random integer from 0 till 2
    # rock: 0, paper: 1, scissors: 2 (as the index in list starts from zero.)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".") # not using comma for computer pick as it adds a space, which we don't want here

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won!", user_wins, "times.")
print("The computer won!", computer_wins, "times.")
print("Goodbye!")