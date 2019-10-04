the_input = "GZOOEHHCTRJYXXVUECLTFFFNKBHYHXXBYYYUUEYYGGLOHHGAAAASCWARRCHWYXXLBIZAAAXXLIWWWWWDDDDDRRHMMPPUUUHZNKKTXACCBJEYUIKHZZDPAKEMRCGCFFHHIIIFDDUUUGFFHR"

count= 0
doubles = []


for i in range(len(list(the_input))):
    doubles.append(the_input[i])

print("\n \n \n")

for i in range(1,len(doubles)):
       if doubles[i-1]==doubles[i]:
            count+=2
       elif doubles[i-1]==doubles[i] == doubles[i+1]:
            count+=3

print(count)

#Indizierung
#>>> txt = "Hello World"
#>>> txt[0]
#'H'
#>>> txt[4]
#'o'
#Statt von vorne kann man die Indizes auch von hinten bestimmen:
#  >>> txt[-1]
#  'd'
#  >>> txt[-5]
#  'W'

#>>> len(txt)
#>>> txt = "Hello World"
#11
#>>> 