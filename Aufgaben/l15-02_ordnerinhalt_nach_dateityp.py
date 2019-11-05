import os
print()

#Schreibe eine Funktion, welche Dir den Inhalt nach dem Typ der Datei sortiert. 
#Konkret sollst Du nach der Dateiendung sortieren. Dazu brauchst 
# Du ein Verzeichnis mir verschiedenen Dateien. Vielleicht eignet sich Dein Downloads Ordner. 
# Vielleicht musst Du aber zum Testen einen Ordner mit verschiedenen Dateien zusammenstellen...

#print_extension_sorted('./test/')
#> jet.mp3
#> racecar.mp3
#> car.mp3
#> hut.png
#> castle.png
#> house.png
#> other_script.py
#> script.py
#> counter.txt
#Dateien mit der Endung "mp3" sind die Ersten, weil alphabetisch m vor p und t ist. 
# Wie vielleicht bemerkt worden ist: Die Dateinamen an sich müssen nicht sortiert sein. 
# Nur der Typ.

def print_extension_sorted(x):
    readytosort = []
    thelist = os.listdir(x)
    final= []
    for i in range(len(thelist)):
        first= thelist[i].find(".")+1
        filetype = thelist[i][first:]
        readytosort.append(filetype+"*"+thelist[i])
    sortedls= sorted(readytosort)
    print(sortedls)
    for a in range(len(sortedls)):
        removercount=sortedls[a].find("*")+1
        remover = sortedls[a][:removercount]
        finisher = sortedls[a].replace(remover,"")
        final.append(finisher)
    return final

print(print_extension_sorted("/Users/Kobain/Downloads/hello"))