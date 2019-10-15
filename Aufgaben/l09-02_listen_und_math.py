the_list = [63, 59, 38, 7, 92, 24, 14, 45, 45, 62, 9, 7, 13, 89, 24, 16, 61, 11, 25, 96]

#THE MAX
for i in the_list:
    themax = 0
    if i > themax:
        themax=i
print(themax, "\n")


#INDEX VON GERADEN ZAHLEN


for i in range(len(the_list)):
    if the_list[i] % 2 !=0:
        print(i, end = " ")
print()

#ARITHMETISCHES
print()
print(sum(the_list)/len(the_list))

#HARMONISCHE MITTEL

harmon = []

for i in the_list:
    b = 1 / i
    harmon.append(b)
print(int(len(the_list)/(sum(harmon))))