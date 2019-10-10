number = 1
dividable = False
while dividable == False:
    dividable = True
    for i in range(1,18):
        if number % i != 0:
            dividable = False
    if dividable == True:
        break
    number += 1
print(number)
 