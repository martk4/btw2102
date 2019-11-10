import json
import os
phonebook = []
def read_file():
    global phonebook
    data = [{"name":"seb","number":732}]
    if os.path.isfile('Aufgaben/phonebook.json') is False:
        f = open('Aufgaben/phonebook.json', 'w')
        phonebook = f.write(json.dumps(data))
        f.close()
    f = open('Aufgaben/phonebook.json', 'r')
    phonebook = json.loads(f.read())
    f.close()
def input_p():
    global phonebook
    read_file()
    key = input("Enter name: ->")
    contact = []
    for i in range(len(phonebook)):
        if key == phonebook[i]["name"]:
            contact.append(phonebook[i])
    if contact !=[]:
        printer = "This is "+key+"'s number: " + str(contact[0]["number"])
        print(printer)
        exit()
    else:
        key2 = input("There is no "+key+"\nEnter number to save "+key+"->")
        saver = {"name": key, "number": key2}
        phonebook.append(saver)
        f = open('Aufgaben/phonebook.json', 'w')
        f.write(json.dumps(phonebook))
        f.close()
        printer = key+"'s number is saved"
        print(printer)
input_p()
