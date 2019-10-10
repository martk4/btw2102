import random
caps = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
lower = "a b c d e f g h i j k l m n o p q r s t u v w y z"
num = "0 1 2 3 4 5 6 7 8 9"
spex= "+ * % & / \ ( ) = ? ! _ - : . ; , $"

c= caps.split(" ")
l= lower.split(" ")
n= num.split(" ")
s= spex.split(" ")

all_c = c+l+s+n

def hallo():
    print ("hallo diana")
def randomizer():
    random_p =random.sample(all_c, 12)
    print("".join(random_p))

for i in range(5):
    randomizer()

