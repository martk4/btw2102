# variable for types of people
types_of_people = 10
# f-string as a variable (ready to print) with variable included
x= f" Ther are {types_of_people} types of people."

#variable
binary = "binary"
#variable
do_not = "don't"
# f-string as a variable with two variables
y = f"Those who kno {binary} and those who {do_not}."

#print f-string
print(x)
print(y)

#print f-strings as variable in another f-string
print(f"I said : {y}") #string in string
print(f"I also said : '{y}''") #string in string

#variable as boolean values
hilarious = False
#variable with empty slot ready to format
joke_evaluation = "Isn't that joke so funny?! {}" #string in string
#print variable with other variable formatted into empty slot
print(joke_evaluation.format(hilarious)) 

#variable ready to print
w = "This is the left side of..."
e = " a string with a right side."

#print two strings after each other
print(w+e)
