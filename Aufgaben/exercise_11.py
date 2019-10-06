
#end = '' tells python not to automatically asume \n 
print("How old are you?", end='')
age = input() # means age = "whatever you type here"
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So,you're {age}, {height} tall and {weight} heavy.")