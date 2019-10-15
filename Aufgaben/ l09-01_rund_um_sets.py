#Nachfolgend hast Du zwei Sets, auf welchen es folgende Eigenschaften zu Berechnen gibt:

#Das Total von:
#Der Differenz zwischen dem Maximum und Minimum der Vereinigungsmenge
#Der Differenz zwischen dem Maximum und Minimum der Schnittmenge
#Die Anzahl der Elemente die nur in einem Set vorkommen
#Hast Du alles richtig gerechnet sollte das Total der Differenzen und die Anzahl der alleinigen Elemente ein 5-faches voneinander sein.

A= {11, 14, 15, 16, 17, 18, 19, 21, 22, 24, 25, 30}
B= {11, 13, 15, 16, 18, 19, 22, 26, 28, 29}

vereinigungsmenge = (A|B)
schnittmenge = (A&B)
symetrische_differenz = (A^B)

print(vereinigungsmenge)

total_v= max(vereinigungsmenge)-min(vereinigungsmenge)
total_s= max(schnittmenge)-min(schnittmenge)
anzahl= len(symetrische_differenz)

print(total_v+total_s)
print(anzahl)

