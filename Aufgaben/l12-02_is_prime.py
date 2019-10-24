def is_prime(x):
    counter = 0
    numbers = [2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        if x % numbers[i] == 0:
            counter += 1
        if x == 1:
            counter += 1
        if x == numbers[i]:
            counter -= 1
    if counter == 0 :
        return True
    return False

print(is_prime(33))






prime = [2, 3, 5, 7, 17, 19, 23, 47, 53, 59, 71, 73, 97]
composite = [4, 10, 9, 21, 64, 1, 99, 51, 49, 0, 62, 77]
for p in prime:
    assert is_prime(p) is True, str(p) + " is prime!"
for c in composite:
    assert is_prime(c) is False, str(c) + " is not prime!"
print('Your function works flawlessly.')