import os

#Schreibe eine Funktion, welche Dir in einer Datei eine Zahl inkrementiert. Z.B.

#increase_counter('counter.txt')
#Bei jeder Ausführung soll die darin enthaltene Zahl um den Wert 1 erhöt werden. 
# Wird also folgendes Programm ausgeführt:

#for i in range(5):
#    increase_counter('counter.txt')
#wird die Zahl 5-mal um 1 erhört und falls der Wert urpsrünglich 0 war, ist er jetzt 5.

#Hinweis: Falls die Datei nicht schon existiert, soll die Funktion einfach annehmen, dass der Wert 0 ist.

#Hinweis2: Kontrollieren ob Deine Lösung funktionert, kannst Du, indem Du die Datei selber öffnest.

f = open('some_file.txt', 'w')
f.write("Hallo Datei.")
f.close()

def increase_counter():
    if os.path.isfile('counter.txt') is False:
        f = open('counter.txt', 'w')
        f.write("0")
        f.close()
    else:
        f = open('counter.txt', 'r')
        reader = f.read()
        number = int(reader)
        print(number)
        f.close()
        writer = number+ 1
        f = open('counter.txt', 'w')
        f.write(str(writer))
        f.close()
    

increase_counter()
