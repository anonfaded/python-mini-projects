import colorama
from colorama import Fore, Style
import random
import time
import sys

colorama.init()

# Function to print a line break with stars
def print_line_break():
    print(Fore.BLUE + "🌟" * 20)
    print(Style.RESET_ALL)

# Function to get user input with specified prompt
def get_user_input(prompt):
    return input(Fore.CYAN + prompt + ": ").lower()

# Function to print game outcome with specified message and color
def print_game_outcome(message, color):
    for letter in message:
        sys.stdout.write(color + letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print(Style.RESET_ALL)
    time.sleep(1)

# Welcome message
print_line_break()
print_ga(Fore.YELLOW + "Welcome to the Mysterious Adventure!".center(40))
print_line_break()
print(Fore.YELLOW + "Your quest begins in the enchanted forest of Avalon.")
print("Your aim is to find the legendary Crystal of Wisdom, hidden deep within the forest.")
print("But beware, the forest is full of secrets and challenges.")
print_line_break()
print(Style.RESET_ALL)

while True:
    name = input(Fore.CYAN + "Type your name: ")
    print(Fore.GREEN + f"Welcome, {name}, to this exciting adventure!\n")
    print(Style.RESET_ALL)

    # Game logic
    found_crystal = False
    while True:
        print(Fore.YELLOW + "You find yourself at a crossroads in the forest.")
        print(Style.RESET_ALL)
        direction = get_user_input("Which way would you like to go? (left/right/straight)")

        if direction == "left":
            print(Fore.YELLOW + "\nYou follow a narrow path through dense foliage.")
            print("After walking for some time, you stumble upon an ancient ruin.")
            print("You can either explore it or continue on your path.")
            print(Style.RESET_ALL)
            action = get_user_input("What will you do? (explore/continue)")

            if action == "explore":
                print_game_outcome("You discover a hidden chamber and find a magical artifact!", Fore.GREEN)
                print("This could be useful on your journey.")
                print("You continue your quest with renewed determination.")
                print_line_break()
                continue

            elif action == "continue":
                print("You decide to leave the ruin behind and continue your journey.")
                print("As you walk deeper into the forest, you sense that you are getting closer to your goal.")
                print_line_break()
                continue

            else:
                print_game_outcome("Not a valid option. Please try again.", Fore.RED)

        elif direction == "right":
            print(Fore.YELLOW + "\nYou venture into a dense thicket of trees.")
            print("The air grows colder as you delve deeper into the darkness.")
            print("Suddenly, you hear a rustling in the bushes.")
            print("You can either investigate or retreat.")
            print(Style.RESET_ALL)
            action = get_user_input("What will you do? (investigate/retreat)")

            if action == "investigate":
                print_game_outcome("You cautiously approach the source of the sound and find a friendly forest creature!", Fore.GREEN)
                print("It offers to guide you through the forest.")
                print("You accept its offer and continue your journey together.")
                print_line_break()
                continue

            elif action == "retreat":
                print("You decide to play it safe and retreat from the thicket.")
                print("You find another path and continue your exploration.")
                print_line_break()
                continue

            else:
                print_game_outcome("Not a valid option. Please try again.", Fore.RED)

        elif direction == "straight":
            print(Fore.YELLOW + "\nYou forge ahead on the main path.")
            print("The trees seem to whisper ancient secrets as you walk.")
            print("Suddenly, you come across a mysterious gate blocking your path.")
            print("You can either try to open it or search for another way.")
            print(Style.RESET_ALL)
            action = get_user_input("What will you do? (open/search)")

            if action == "open":
                print_game_outcome("You try to open the gate, but it's locked tight.", Fore.RED)
                print("You decide to search for another way around.")
                print_line_break()
                continue

            elif action == "search":
                print_game_outcome("You search the area and find a hidden lever!", Fore.GREEN)
                print("You pull the lever and the gate swings open, revealing a path forward.")
                print("You walk through the gate and continue your journey.")
                print_line_break()
                continue

            else:
                print_game_outcome("Not a valid option. Please try again.", Fore.RED)

        else:
            print_game_outcome("Not a valid option. Please try again.", Fore.RED)

        # Check if player has found the Crystal of Wisdom
        if random.random() < 0.2:  # 20% chance of finding the crystal in each step
            found_crystal = True
            break

    # Game outcome
    if found_crystal:
        print_line_break()
        print_game_outcome("Congratulations, you have found the Crystal of Wisdom!", Fore.GREEN)
        print("You have completed your quest and become the hero of Avalon!")
    else:
        print_line_break()
        print_game_outcome("You search tirelessly, but the Crystal of Wisdom eludes you.", Fore.RED)
        print("Your quest continues...")

    # Ask if the player wants to play again
    play_again = get_user_input("\nDo you want to embark on another adventure? (yes/no)")
    if play_again != "yes":
        print_line_break()
        print(Fore.YELLOW + "Thank you for playing! Until next time, brave adventurer!")
        print_line_break()
        break
