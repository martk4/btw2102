###############################################################
#               SET UP
###############################################################

import time
import sys

###############################################################
#               Design
###############################################################

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

###############################################################
#               INTRO
###############################################################

def header():
    print("\n")
    print(colors.fg.green, "\t\tHELLO USER" ,colors.reset)
    for i in range(21):
        print("*", end=" ") 
    print(colors.fg.green,"\n\tWelcome to the game of NIM",colors.reset)
    for i in range(21):
        print("*", end=" ") 
    print()
    time.sleep(1.5)
    print("\n\n")

def loader():
    print("LOADING")
    print()
    text= "#########################################"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def rules():

    print(colors.fg.green,"\n\tTHE RULES OF THE GAME",colors.reset)
    print("""\nTheres a heap of 20 Stones.
    On each turn you may draw 
    1 or 2 stones from the heap.
    So does your opponent.""")
    print(colors.bg.red,"The player drawing the last stone loses.",colors.reset)
    time.sleep(2.5)

    print()
    print("You may quit the game at any time\nby entering", end=" ")
    print(colors.bg.red,"q",colors.reset, end=" ")
    print("as input.")
    print("Enter", end=" ")
    print(colors.bg.green,"n",colors.reset, end=" ")
    print("to start a new game. ")

header()
loader()
rules()

###############################################################
#               GAME 
###############################################################

def game_loop():
    def winner():
        print("YOU WON")
        print("How about another game?")

    def loser():
        print("YOU LOST")
        print("How about another game?")
    
    heap_count= 20

    while True:
        key = input("Your input:")
        if key == "q":
            print ("See you soon. Goodbye!")
            break

        elif key == "n":
            print("Starting a new game.")
            while True:
                print(f"There are {heap_count} stones on the heap.\nHow many would like to draw? 1 or 2?\n")
                key = input("Your input:")
                if key == "q":
                    break
                if heap_count == 1:
                    print("You lost")
                    break
                elif key == "1":
                    heap_count -=1
                    print(f"You drew 1 Stone.")
                    if heap_count == 1:
                        print("You won")
                        break
                elif key == "2":
                    heap_count -=2
                    print(f"You drew 2 Stone.")
                    if heap_count == 1:
                        print("You won")
                        break
                else:
                    print("Sorry, I don't understand your input.\nPlease try again.")
        
        
        print ("See you soon. Goodbye!")
        break
    
    else:
        print("Sorry, I don't understand your input.\nPlease try again.")
        
game_loop()

###############################################################
#               AI PLAYER 
###############################################################

def choose_player():
    print("Please choose your opponent")
    print(colors.fg.yellow, "\t1 : Goofy the Goof",colors.reset)
    print(colors.fg.purple, "\t2 : Sherlock Holmes",colors.reset)

