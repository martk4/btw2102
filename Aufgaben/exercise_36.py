#To DO 
 
# plan gametype
# plan rooms
# create enviroment 
# create rooms
# create game loop
# design GUI

#enviroment
import sys
import time

#menu
def new_game():
    for i in range(30):
        print()
    print("Welcome Player\nYou wake up alone in a strange room\nSlowly you realize,that you've been captured by a psycho killer\nTo escape certain death you need to solve the rittles the killer left for you!\n\nGood Luck!")
    print("Are you ready?")
    yes_no = input("y/n?")
    while True:
        if yes_no == "y":
            room_math()
        elif yes_no== "n":
            quitter()
        else:
            print("Wrong input.Try again")
    room_planet()
def quitter():
    print("Sad to see you leave. Bye")
    exit()
def game_over():
    print("GAME OVER\nStart a new game?")
    while True:
        yes_no = input("y/n?")
        if yes_no == "y":
            new_game()
        elif yes_no== "n":
            quitter()
        else:
            print("Wrong input.Try again")

#rooms
def room_freedom():
    print("Congratulations. You're save!")
    print("See you soon.")
    exit()
def room_planet():
    print("""
    On the ceiling is a large painting.
    It shows a roman warrior with a sword, he seems to be praying.
    At the door is a terminal. It says:
    You can open the door by entering a planet. You have 3 tries.
    """)
    
    tries = 3
    while tries > 0:
        mars = input("Type Planet Name:")
        right_planet = ['mars','Mars','MARS']
        wrong_planet = ['Mercury','mercury','MERCURY', 'VENUS','Venus','venus','EARTH','Earth','earth','Jupiter', 'jupiter','JUPITER','SATURN','saturn','Saturn','Uranus','URANUS','uranus','NEPTUN','neptun','Neptun',]
        if mars == "q" :
            quitter()
        elif mars in right_planet:
            print("Right Planet.The door opens.\nYou see the sun shining from a beautiful sky\nand stroll calmly into freedom.")
            room_freedom()
        elif mars in wrong_planet:
            tries -= 1
            print("Wrong planet\nYou have",tries,"tries left.")
        else:
            tries -= 1
            print(f"This is not a planet. {tries} left.")
    print("You fall through a trapdoor in a snakepit and die.")
    game_over()
def room_math():
    print()
    print("It's a dark room. Numbers are projected unto a wall.\nNext to the door you find a keyboard.'Are you ready to memorize numbers,dear?' ")
    while True:
        yes_no = input("y/n?")
        if yes_no == "y":
            break
        elif yes_no== "n":
            quitter()
        else:
            print("Wrong input.Try again")
    tries = 3
    while tries > 0:
        print("Remember you have {} tries left".format(tries))
        time.sleep(3)
        number_list= ["2","8","9","11"]
        for c in number_list:
            for i in range(30):
                print()
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.5)
            for i in range(30):
                print()
        summe= input("Enter sum of all the numbers you've seen:")
        if summe == "q":
            quitter()
        elif summe == "30":
            print("\n")
            print("Very well, a door opens and you enter a new room.")
            room_planet()
        else:
            print("Wrong answer!")
            tries -=1
    print("YOU HAVE NO MORE TRIES. You are vacuumed into space and die!")
    game_over()
    
#run it
new_game()