#Nachfolgend hast Du 2 Dictionaries. Das Ziel ist die gesammten Kosten für Deinen Einkauf zu berechnen. Im einen dict hast Du die Anzahl der Früchte die Du kaufen möchtest. Im zweiten dict hast Du die dazugehörigen Preise.

#Die Lösung ist durch 7 teilbar.

amount = {
    "banana": 6,
    "apple": 2,
    "orange": 12,
    "kiwi": 3
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1,
    "kiwi": 3
}

total = 0
for a in amount:
    for b in prices:
        if a == b :
            total += amount[a]*prices[b]
print(total)