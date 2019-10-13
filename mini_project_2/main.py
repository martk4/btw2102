###############################################################
#               SET UP                                        #
###############################################################

import time
import sys
import random

###############################################################
#               Design                                        #
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
#               INTRO                                         #
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
def quitter():
    print ("See you soon. Goodbye!")
    exit()
def newer():
    global heap_count
    print("Starting a new game", end = "    ")
    text= ". . ."
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)
    heap_count = 20
    print("\n\n\n")
    counter()
def menu_choice():
    while True:
        key = input("Your input:")
        if key == "q":
            quitter()
        elif key == "n":
            newer()
        else:
            print("Sorry, I don't understand your input.\nPlease try again.")


###############################################################
#               GAME                                          #
###############################################################
heap_count= 20

def winner():
    print(colors.bg.green,"YOU WON",colors.reset)
    exit()

    exit()
def loser():
    print(colors.bg.red,"YOU LOST",colors.reset)
    exit()
def counter():
    global heap_count
    if heap_count == 20:
        print(f"There is a heap of {heap_count} stones.")
    elif heap_count <= 19:
        print(f"There are {heap_count} stones on the heap.")
    print("Would you like to remove 1 or 2 stones?")
    print()
    game()
def game():
    global heap_count
    while True:
        key = input("Your input:")
        if key == "q":
            quitter()        
        elif key == "1":
            heap_count -= 1
            print(f"There are now {heap_count} stones on the heap.")
            break
        elif key == "2":
            heap_count -= 2
            print(f"There are now {heap_count} stones on the heap.")
            break
        elif key == "n":
            newer()
        #if heap_count == 1:
            #winner()
        else:
            print("Sorry, I don't understand your input.\nPlease try again.")
    if heap_count <= 1:
        winner()
    ai_player()
        
###############################################################
#               AI PLAYER                                     #
###############################################################

def choose_player():
    print("Please choose your opponent")
    print(colors.fg.yellow, "\t1 : Goofy the Goof",colors.reset)
    print(colors.fg.purple, "\t2 : Sherlock Holmes",colors.reset)

def ai_player():
    global heap_count 
    print()
    print("AI calculates next move", end = "    ")
    text= ". . ."
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")
    a_choice= [1,2]
    a= random.choice(a_choice)
    
    if a == 1 :
        print(f"AI drew 1 stone.")
        heap_count -= 1
    if a == 2:
        print(f"AI drew 2 stones.")
        heap_count -=2
    print()
    if heap_count <= 1:
        loser()
    counter()


###############################################################
#               RUN IT                                        #
###############################################################


header()
loader()
rules()
menu_choice()
