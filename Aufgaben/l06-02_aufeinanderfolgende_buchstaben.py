the_input = "GZOOEHHCTRJYXXVUECLTFFFNKBHYHXXBYYYUUEYYGGLOHHGAAAASCWARRCHWYXXLBIZAAAXXLIWWWWWDDDDDRRHMMPPUUUHZNKKTXACCBJEYUIKHZZDPAKEMRCGCFFHHIIIFDDUUUGFFHR"
#counter
count= 0
#lister
doubles = []

#read out string as a list
for i in range(len(list(the_input))):
#add to doubles list
    doubles.append(the_input[i])

print("\n \n \n")
# for every i in the list from the first until the last character
for i in range(1,len(doubles)):
     # if i in doubles is exactly the same as i-1 (character before)
       if doubles[i-1]==doubles[i]:
            #add 2 to the count
            count+=2
       elif doubles[i-1]==doubles[i] == doubles[i+1]:
            count+=3

#spit it
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