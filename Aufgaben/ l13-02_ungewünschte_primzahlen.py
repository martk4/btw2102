print("\n\n")
def is_prime(x):
    counter = 0
    numbers = [2,3,4,5,6,7,8,9]
    for b in range(len(numbers)):
        if x % numbers[b] == 0:
            counter += 1
        if x == 1:
            counter += 1
        if x == numbers[b]:
            counter -= 1
    if counter == 0 :
        return True
    return False
removal = []

def remove_primes(y):
    for i in range(len(y)):
        x = int(y[i])
        if is_prime(x) == True:
            removal.append(int(y[i]))
    for p in removal:
        if p in input_list:
            input_list.remove(p)
    return len(removal)



input_list = list(range(1, 41, 2))
print(remove_primes(input_list))
remove_primes(input_list)
print(input_list)
count = remove_primes(input_list)
assert input_list == [1, 9, 15, 21, 25, 27, 33, 35, 39], "Primes not correctly removed."
assert count == 11, "Return value is incorrect."
print("Your function works flawlessly. Nice job!")

