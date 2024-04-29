import sys
import time
from colorama import Fore, Style, Back
import os
import subprocess

# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Play sounds thru mpv player for realistic effect 
def play(sound_file):
    """
    Play the specified sound file using mpv.

    Args:
        sound_file (str): The name of the sound file to be played (without the directory).
        audio_dir (str, optional): The directory where the audio files are located. Defaults to "audios/".
    """
    mpv_path = "mpv"  # Modify this to the path of the mpv executable if necessary
    full_path = sound_file
    subprocess.Popen([mpv_path, '--no-terminal', full_path], stdin=subprocess.PIPE)

# Function to print slow text
def print_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04) # positive number: slow, negative number: fast

def print_walk(text):  
    print_slow(Fore.YELLOW + text)
    time.sleep(1)
    print_slow(".")
    time.sleep(1)
    print_slow(".")
    time.sleep(1)
    print_slow(".\n\n" + Style.RESET_ALL)
    time.sleep(1)

# Function to print grayed colored text
def print_gray(text):
    print(Style.DIM + text + Style.RESET_ALL)
# Function to print blued colored text
def print_blue(text):
    print(Fore.CYAN + text + Style.RESET_ALL)
# Function to print red colored text
def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)

# Function to print yellow colored text
def print_yellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

# Function to simulate a pause for dramatic effect
def dramatic_pause():
    time.sleep(1)

# Function to simulate progress bar
def print_progress_bar(current_progress, target_progress):
    bar_length = 20
    progress_length = int(bar_length * current_progress)
    bar = '[' + Fore.GREEN + '#' * progress_length + Fore.RESET + ' ' * (bar_length - progress_length) + ']'
    print("\rProgress:", bar, f"{current_progress * 100:.0f}%", end='', flush=True)
    
    if current_progress < target_progress:
        increment = 0.01  # Adjust increment value as needed
        while current_progress < target_progress:
            current_progress += increment
            if current_progress > target_progress:
                current_progress = target_progress
            progress_length = int(bar_length * current_progress)
            bar = Fore.MAGENTA + '[' + Style.RESET_ALL + Fore.GREEN + '#' * progress_length + Fore.RESET + ' ' * (bar_length - progress_length) + Fore.MAGENTA + ']' + Style.RESET_ALL
            print(Fore.MAGENTA + "\rProgress:" + Style.RESET_ALL, bar, f"{Fore.GREEN}{current_progress * 100:.0f}%{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.1)  # Adjust sleep time as needed
        

    else:
        print()  # Move to next line when progress reaches 100%



# Introduction
def intro():
    clear_terminal()
    time.sleep(0.1)
    play("audios/computer/intro/Welcome_whats_your_name.mp3")
    print_slow(Fore.GREEN+"Welcome to The Tale of Fadedhood adventure game!"+ Fore.LIGHTMAGENTA_EX+"\tbeta version 0.2\n\n" + Style.RESET_ALL)
    time.sleep(0.5)
    # Player name
    name = input(Fore.CYAN + "Survivor, what's your name?: " + Style.RESET_ALL).strip()

    # Greetings audio
    play("audios/computer/intro/Greetings!.mp3")
    time.sleep(0.5)

    print(Fore.CYAN + f"Greetings, {Fore.YELLOW}{name}{Fore.CYAN}! Prepare yourself for an epic adventure!" + Style.RESET_ALL + "\n")
    time.sleep(2.2)
    # Add realistic response to finding the walkie talkie
    
    print_slow(f"{Fore.YELLOW}{name}{Style.RESET_ALL}: Whoa... What's that at my feet?\n")
    play("audios/player/intro/Whoa..._Whats_that.mp3")
    time.sleep(0.7)
    print(Fore.GREEN + r"""
                  .              . .'.    
            \   /      .'. .' '.'   
          -=  o  =-  .'   '              
            / | \                        
            |                           
            |=====.               
            ||=o=||              
            ||___||               
            |[:::]|                
            '-----'
    """ + Style.RESET_ALL )
    

    # Add dramatic effect - player finds a walkie talkie
    time.sleep(1.5)
    print_slow(f"{Fore.YELLOW}{name}{Style.RESET_ALL}: Bent down and picked it up, revealing a walkie-talkie.😯\n\n")

    # Add dramatic effects in text for the message from the walkie talkie
    time.sleep(0)
    print_slow(f"{Fore.YELLOW}{name}{Style.RESET_ALL}: 📻📡 The walkie-talkie emits a mysterious sound... 📡📻\n\n")

    # Simulate suspenseful pause
    time.sleep(2)
    clear_terminal()

    # Display message from walkie talkie with dramatic effect
    play("audios/computer/intro/Listen_up!!.mp3")
    print(Fore.GREEN+ r"""
                                                         ▓▓▓         
                     ░░                                 ▓▓▓▓         
                   ░░░ ░                                 ▓▓▓▓▓▓      
                    ░░░░░                                ▓▓▓▓        
                     ░░                            ▓▓▓▓▓ ▓▓▓▓▓▓▓     
           ▓    ░░░░ ░░░░░                            ▒▓▓▓▓▓▓▓▓▓     
         ▓▓▓▓   ░░░░░░░░░░░  ▓▓▓                      ▒▓▓▓▓▓ ▓▓      
        ▓▓▓▓▓    ░░░░░░     ▓▓▓▓▓                     ▓ ▓▓▓▓▓▓▓▓▓▓▓  
        ▓▓▓▓▓▓▓ ░ ░  ░░░░░░▓▓▓▓▓▒   ░              ▓▓▓▓▓▓▓▓▓▓▓       
     ▓▓▓▓▓▓▓▓▓▓▓▓░░░ ░░ ▓▓▓▓▓▓▓▓▓░░░░░ ░               ▓▓▓▓▓▓▓▓▓▓▓▓  
      ▓▓▓▓▓▓▓▓▓▓▓ ░░░░░░░░▒▓▓▓▓▓▓▓▓░░░░        ▓▓▒▓ ▒▓    ▓▓▓        
      ▓▓▓▓▓▓░░░░░░░░░░░ ▓▓▓▓▓▓▓▓▒░░░░           ▓▓ ▓▓▓▓▓▓▓▓▓▓        
    ▓▓▓▓▓▓▓▓▓▓░▓▓  ░░░░░░▒▒▓▓▓▓▓░░░░░                ▓▓▓▓▓▓▓▓        
      ▓▓▓▓▓▓▓▓▓▓░░ ░░░░░░ ▓▓▓▓▓░░░░░░░░░              ▓▓▓▓▓▓▓▓▓▓▓▓   
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓░░░                 ▓▓▓▓▓▓▓      
   ▓▓▓▓▓▓▓▓▓▓▓▓▓░▒░░░░░░▓░░▓▓▓▓▓▓▓▓░░░░░               ▓▓▓▓▓▓▓       
    ▓  ▓▓▓▓▓▓▓▓ ▒░░░░░░░░▒▓▓▓░▒▓▓░▓░░░░░░░          ▓▓▓▓▓▓▓▓▓▓▓     
     ▒▓▓▓▓▓▓▓▓▓▓   ░░░  ░▓▓▓▓▓▓▓▓▓▓▓░                   ▓▓▓          
         ▓▓          ░▓▓▓▓▓▓▓▓ ░▓▓▒░░░░░░░                ▓          
         ▓▓          ░      ▓▓      ░                     ▓          
                     ░      ▓▓     ░░                     ▓▒  
    """ + Style.RESET_ALL)
    print_slow(f"\t📻 > {Fore.CYAN}Listen up, {Fore.YELLOW}{name}{Style.RESET_ALL}{Fore.CYAN}! You're now deep in the wilderness, stranded in the unknown. \n{Fore.GREEN}Your mission:{Style.RESET_ALL} {Fore.CYAN}Find a way out of this forest and uncover the hidden town of Fadedhood. \nGet ready to navigate through 5 challenging levels. Time is of the essence, danger lurks\naround every corner, and the forest holds many secrets...\n\n{Style.RESET_ALL}")
    time.sleep(6)
    print_slow(f"{Fore.YELLOW}{name}{Style.RESET_ALL}: Hello!?... Who is that?!!!!\n\n")
    play("audios/player/intro/Hello_Whose_that.mp3")

    time.sleep(5)
    print_slow(f"{Back.RED} Silence... Connection dropped- {Style.RESET_ALL}⛔\n\n")



    # Prompt the player if they are ready to start their journey
    time.sleep(5)
    play("audios/computer/intro/ready_to_escape_forest.mp3")
    ready = input(Fore.CYAN + f"Are you ready to start your journey of escaping the forest, {Fore.YELLOW}{name}{Fore.CYAN}?{Style.RESET_ALL} {Fore.YELLOW}(yes/no)" + Style.RESET_ALL+": ")
    if ready.lower() == "yes":
        print(f"{Fore.YELLOW}\nLet the adventure begin!\n{Style.RESET_ALL}")
        time.sleep(3)
    else:
        print(f"{Fore.YELLOW}\nTake your time, adventurer. Your journey awaits when you're ready.\n{Style.RESET_ALL}")
        quit()
    return name 



# Function for Level 1
def level_1():
    clear_terminal()
    # print(name)
    print_slow(Fore.YELLOW + "Level 1: The Journey Begins")
    time.sleep(0.5)
    print(Fore.GREEN+ r"""
                            ,@@@@@@@,
                    ,,,.   ,@@@@@@/@@,  .oo8888o.
                 ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
                ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
                %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
                %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
                `&%\ ` /%&'    |.|        \ '|8'
                    |o|        | |         | |
                    |.|        | |         | |
                 \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
    """ + Style.RESET_ALL)
    time.sleep(0.5)
    # play("audios/computer/level1/level1-intro.mp3") remove comment
    print(Fore.CYAN + "You're in a thick forest surrounded by tall trees. Ahead, the path is completely blocked by bushes and fallen trees.\nTo your left, there's a river with shimmering water, but it's said to be dangerous. On the right, there's a narrow\npath that looks passable, but it's overgrown with bushes and roots.\n\n" + Style.RESET_ALL) # add the _slow after done
    # time.sleep(6) remove this comment after done

    while True:
        choice = input(f"What will you do? {Fore.YELLOW}(left/right/ahead){Style.RESET_ALL}: ").lower()
        if choice == "left":
            clear_terminal()
            print(Fore.GREEN + r"""
                                 _.._
                  _________....-~    ~-.______
                 ~~~                            ~~~~-----...___________..--------
                                                            |   |     |
                                                            | |   |  ||
                                                            |  |  |   |
                                                            |'. .' .`.|
                 ___________________________________________|0oOO0oO0o|____________
                -          -         -       -      -    / '  '. ` ` \    -    -
                      --                  --       --   /    '  . `   ` \    --
                ---            ---          ---       /  '                \ ---
                     ----               ----        /       ' ' .    ` `    \  ----
                -----         -----         ----- /   '   '        `      `   \
                      -----          ------     /          '    . `     `    `  \
                            -------           /  '    '      '      `
                                    --------/     '     '   '                            
            """)
            play("audios/sound-effects/walking-through-leaves.mp3")
            time.sleep(1)
            print_walk("Walking")
            time.sleep(1) # in below line add the _slow when level 1 is done
            play("audios/sound-effects/player_got_on_left_path.mp3")
            print(Fore.CYAN + "You venture down the left path and encounter a wide river blocking your way.\n"
               "It seems impossible to cross the river without a boat.\n"
               "Perhaps it's best to go back and explore another path, " +  ".\n\n" + Style.RESET_ALL) # add name + for tha player name to be added.
            while True:
                go_back = input(f"You must go back! {Fore.YELLOW}(walk/stay){Style.RESET_ALL}: ").lower()
            
                if go_back == "walk":
                    play("audios/sound-effects/walking-through-leaves.mp3")
                    time.sleep(1)
                    play("audios/player/level1/uhh_im_lost.mp3")
                    print_walk("Walking back")
                    time.sleep(1)
                    clear_terminal()
                    print(Fore.GREEN+ r"""
                                            ,@@@@@@@,
                                    ,,,.   ,@@@@@@/@@,  .oo8888o.
                                 ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
                                ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
                                %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
                                %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
                                `&%\ ` /%&'    |.|        \ '|8'
                                    |o|        | |         | |
                                    |.|        | |         | |
                                 \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
                    """ + Style.RESET_ALL)
                    print(Fore.CYAN + "You're in a thick forest surrounded by tall trees. Ahead, the path is completely blocked by bushes and fallen trees.\nTo your left, there's a river with shimmering water, but it's said to be dangerous. On the right, there's a narrow\npath that looks passable, but it's overgrown with bushes and roots.\n\n" + Style.RESET_ALL) 
                    break
                else:
                    play("audios/player/level1/i_need_to_escape_not_stay.mp3")
                    print_blue("You got nothing to do here!\n")
                    continue
            continue
            # swim_choice = input("Will you swim across the river? (yes/no): ").lower()
            # if swim_choice == "yes":
            #     print("You bravely swim across the river and reach the other side.")
            #     print_yellow("Congratulations! You've completed Level 1.")
            #     print("The journey continues...")
            #     print_progress_bar(0.2)  # Assuming completion of Level 1 represents 20% progress
            #     break
            # elif swim_choice == "no":
            #     print("You decide not to risk swimming across the river.")
            #     print("The journey continues...")
            #     break
            # else:
            #     print("Invalid choice. Please try again.")
        elif choice == "right":
            print_blue("You cautiously tread along the narrow path to the right.")
            print("You are done")
            print_progress_bar(0.0, 0.2)  # Increase from 0% to 20%
            input("\nWould you continue or not")
            break
        elif choice == "ahead":
            play("audios/player/level1/i_cant_climb_the_bushes.mp3")
            print_slow(Fore.RED + "Path Blocked :(\n\n" + Style.RESET_ALL)
            time.sleep(0.5)
            # print("The journey continues...")
        else:
            print_red("Invalid choice. Please try again.")

    # print("You are done")
    # print_progress_bar(0.0, 0.2)  # Increase from 0% to 20%
    # input("\nWould you continue or not")











# Start intro and Level 1
# name = intro()
# level_1(name) also add the name variable in the function if its needed for using
level_1()
# print_progress_bar(0.4, 0.8)  # Increase from 20% to 40%
