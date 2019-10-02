#Beispiel:

#0101 0101

#64 + 16 + 4 + 1 = 85
#Zu rechnen:

#0110 0110 = 
a = 64+32+4+2
#1111 1110
b = 128+64+32+16+8+4+2
#0000 1111
c = 8+4+2+1
#1010 0101
d = 124+32+4+1

print(a,b,c,d)
#Kontrolliere deine Lösungen mit Hilfe vom Python-Interpreter, indem Du die ausgerechnete Zahlen eingibst. Nutze die Funktion bin() um die Zahl in Binär umzuwandeln. Starten kannst du den Interpreter mit py oder python3 und mit exit() wieder stoppen.

a1= bin(a)
b1= bin(b)
c1= bin(c)
d1= bin(d)


print(a1,b1,c1,d1)

#$ python3 oder PS> py
#>>> bin(85)
#0b01010101
#>>> exit()