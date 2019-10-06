#set value for variable people
people = 30
#set value for variable cars
cars = 40
# set value for variable trucks
trucks = 15

#if statement as condition (more cars than people)
if cars > people:
    print("We should take the cars")

# else if statement as codition if the statements before were False 
elif cars < people:
    print("We should not take the cars.")

#if non statement of the above is True, then do this:
else:
    print("We can't decide.")

if trucks > cars: 
    print("Thats too many trucks.")

elif trucks<cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide!")

if people > trucks:
    print("Alright,let's just take the trucks")

else: 
    print("Fine, let's stay home then!")