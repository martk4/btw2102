start = """ You enter a dark room with two doors.
Do you go through door 1,2, or 3? """

print(start)

door = input("-->")

if door == "1":
    print(""" You enter a bright room, there 's a giant bear eating a 
    cheese cake\nWhat do you do?""")
    print("""1. Take the Cake.\n2. Scream at the bear.""")

    bear = input("-->")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss ar Cthulhu's retina.")
    print("""1. Blueberries \n2. Yellow jacket clothespins
    \n3. Understanding revolvera yelling melodies""")

    insanity = input("-->")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.\nGood Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good Job")

elif door == "3":
    print(start)
    print("You're in a endless loop. Good Job!")
    

else:
    print("You stumble around and fall on a knife and die. Good Job!")