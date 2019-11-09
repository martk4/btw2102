#Das Ziel dieser Aufgabe ist eine Telefonbuch App zu schreiben. 
# Wenn die App gestartet wurde, fragt sie nach dem Namen. 
# Ist der Name bereits im Telefonbuch abgelegt, 
# so kommuniziert sie das und gibt die entsprechende Nummer aus. 
# Falls die Nummer noch nicht gespeichert wurde, 
# fragt die App nach der Nummer und der Benutzer kann diese eingeben.

#Als Beispiel könnte dies so aussehen:

#python3 phonebook.py 

#Phonebook APP!
#Give me a name: seb
#I couldn't find seb.
#Give me the number and I save it: 345

#python3 phonebook.py 

#Phonebook APP!
#Give me a name: seb
#I have found seb!
#The number is: 345
#Um die Daten persistent zu haben sollst Du mit Dateien und JSON Arbeiten. Der Inhalt der JSON-Datei kann zum Beispiel wie folgt aussehen:

#[
#    {
#        "name": "tynx",
#        "number": "123"
#    },
#    {
#        "name": "seb",
#        "number": "345"
#    }
#]