#Studiere nachfolgendes Beispiel, führe es aus und konsultiere die offizielle Dokumentation für detailierte Informationen.

name = "Peter"
age = 23

print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

#Vervollständige nachfolgendes Program aufgrund der Kommentare. Nur innerhalb der geschweiften Klammern {} sollen Änderungen angebracht werden.

number=23
float_number = 1/3
text= "hello"

# next statement should print 023
print("{0:03.0f}".format(number))

# Next statement should only print 0.33
print("{0:3.2f}".format(float_number))

# Next statemen should print: ****hello****
print('{0:*^13}'.format(text))

print("\n DONE")