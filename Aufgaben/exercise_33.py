i=0
numbers=[]

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    print("What should I add to the number?")
    in_num = input("->")
    i = i + int(in_num)
    print("Numbers now:", numbers)
    print(f"At the botom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
