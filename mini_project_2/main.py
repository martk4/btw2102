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
    class fg:
        red='\033[31m'
        green='\033[32m'
        blue='\033[34m'
        yellow='\033[93m'
    class bg:
        red='\033[41m'
        green='\033[42m'


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
        time.sleep(0.25)
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
    print("There is only 1 stone left.")
    print(colors.bg.green,"YOU WON",colors.reset)
    exit()

    exit()
def loser():
    print("There is only 1 stone left.")
    print(colors.bg.red,"YOU LOST",colors.reset)
    exit()
def counter():
    global heap_count
    if heap_count == 20:
        print(colors.bold, f"There is a heap of {heap_count} stones.", colors.reset)
    elif heap_count <= 19:
        print(colors.bold,f"There are {heap_count} stones on the heap.",colors.reset)
    print("Would you like to remove 1 or 2 stones?")
    print()
    game()
def game():
    global heap_count
    if heap_count == 2:
        while True:
            key = input("Your input:")
            if key == "q":
                quitter()        
            elif key == "1":
                heap_count -= 1
                if heap_count <= 1:
                    winner()
                else:
                    print(f"There are now {heap_count} stones on the heap.")
                    break
                break
            elif key == "2":
                print("To win the game you must draw 1 Stone. Try again")
            elif key == "n":
                newer()
            else:
                 print("Sorry, I don't understand your input.\nPlease try again.")
        ai_player()
    else:    
        while True:
            key = input("Your input:")
            if key == "q":
                quitter()        
            elif key == "1":
                heap_count -= 1
                if heap_count <= 1:
                    winner()
                else:
                    print(f"There are now {heap_count} stones on the heap.")
                    break
                break
            elif key == "2":
                heap_count -= 2
                if heap_count <= 1:
                    winner()
                else:
                    print(f"There are now {heap_count} stones on the heap.")
                    break
                break
            elif key == "n":
                newer()
            else:
                 print("Sorry, I don't understand your input.\nPlease try again.")
        if heap_count <= 1:
            winner()
        ai_player()
        
###############################################################
#               COMPUTER PLAYER                               #
###############################################################

def ai_player():
    global heap_count 
    print()
    print("Computer calculates next move", end = "    ")
    text= ". . ."
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
    print("\n")
    
    if heap_count >= 7:
        a_choice= [1,2]
        a= random.choice(a_choice)
        if a == 1 :
            print(f"Computer drew 1 stone.")
            heap_count -= 1
            print()
        if a == 2:
            print(f"Computer drew 2 stones.")
            heap_count -=2
            print()
        if heap_count <= 1:
            loser()
        counter()
    elif heap_count == 2:
        print(f"Computer drew 1 stone.")
        heap_count -= 1
        loser()
    elif heap_count == 3:
        print(f"Computer drew 2 stones.")
        heap_count -= 2
        loser()
    elif heap_count == 4:
        print(f"Computer drew 1 stone.")
        heap_count -= 1
        counter()
    elif heap_count == 5:
        print(f"Computer drew 1 stones.")
        heap_count -= 1
        counter()
    elif heap_count == 6:
        print(f"Computer drew 1 stones.")
        heap_count -= 1
        counter()

 
###############################################################
#               RUN IT                                        #
###############################################################

header()
loader()
rules()
menu_choice()
