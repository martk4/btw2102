long_calculation = "8 +1 -4 +2 -4 -2 +1 -3 +2 -2 +5 +2 +4 +1 -2 +3 -4 +1 -5 +4 -5 -1 -5 +5 -3 -5 -5 -5 -4 +1 +4 +4 -1 -5 -4 -5 -2 +3 -5 -4 +5 -2 -1 +1 +1 +5 +2 +3 -4 -1 +4 +2 +3 +3 -1 +4 +1 +5 +2 +4 +1 +2 +5 +2 +2 -2 +5 +3 +5 +1 -3 -3 +1 +2 -4 +5 +2 +4 +2 -4 -2 -2 -3 -3 -3 -5 -1 -3 +2 -1 +3 -2 -4 -1 +3 -2 -2 -2 -1 -5 -2 +5 -2 +4"

#Break up into Elements on " "
b = long_calculation.split(" ")

#counter in listform
plussum = []
negssum = []

for i in b: 
    if "+" in i:
        i2= i.replace("+","")
        plussum += i2

    elif "-" in i:
        z2= i.replace("-","")
        negssum += z2
    else:
        plussum +=i

#convert string into integers
psum = sum(int(i) for i in plussum)
nsum = sum(int(i) for i in negssum)
#spit
print(psum-nsum)
