for i in range (1,100,1):
    if i%3==0:
        print("fizz")
        if i%5==0:
            print ("fizzbuzz")
            continue
    elif i%5==0:
        print("buzz")
        if i%3==0:
            print("fizzbuzz")
            continue

    else:
        print(i)


for i in range (1,100,1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        
    if i%5==0:
        print ("buzz")
        continue
          
    if i%3==0:
        print("fizz")
        

    else:
        print(i)