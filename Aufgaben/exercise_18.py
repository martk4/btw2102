# takes as many arguments as you want:
def print_four(*args):
    arg1,arg2,arg3,arg4, = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3 {arg3}, arg4 {arg4}")

# this is simpler

def print_four_again (arg1,arg2,arg3,arg4):
    print(f"arg1: {arg1}, arg2:{arg2}, arg3: {arg3}, arg4: {arg4}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_nothing():
    print("I got nothing")

print_four(1,2,3,4)
print_four_again(1,2,3,4)
print_one(1)
print_nothing()


