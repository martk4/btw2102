ids = """KGTMEPNQGDXBWQZQ
PAKONFLCBGQDUZIG
HESGJHHRZLPYFAOD
PSCKWKJTLNRUKEIH
UWCELSKZRVRNROYG
FEWRPYGKAXHTLRYY
FBJQOSBWGXNHULVR
YCNWGFPXAEAIWAUQ
TFIVSAKWMXUBPNLJ
BWQTGSFCAZVCCYOK
JHPJBWDAJIEJSKTZ
QOCEVEZIPTXRDGWA
HVGFJUVYVAKQIXMB
WNNUBDKXPZRNVQGO
EJCYSHMLVFFGDBXW
ODQQQHNYMUKXZVRX
IQJCLTYWNZFHBXVA
PKVDARGMBUJKWKNG
HISBEQSYVFWKMSXT
DUXTOAMVKVEHVYRB
NEJTSACYIUBKDIHM
VIHFOKMEDRYSPATX
GTFMVKBSLOKDXKSQ
FQOJLFYRECUHBXDF
CFOVKMSBXHPAOWOS
AMKHSEBZPRGYPWPC
FUTCNCUHXSDGYOUL
DOLWDFZPTDKHUVYA
CJEOAHYVQGKMXAUD
TAFCXGETDYTUJLPJ
ARMKIVEFKDHWKGMX
FTIQBAEVMGNUSLZW
FYKTCUVDRFZGSHIF
SVUHPUKMYTRAJVVL
BLQNXKTTCIUJOOWO
ZTWJBLROTATGEPNM
TMWOSVFLKIRBAEFH
GHJHFPDKOHMVZAUB
HTCVUEQGHQYJKQWL
LBJNQDWVRAJJPMPX
CKLWPNDAHICVSGCJ
HVXNSTGPAMAOKDRA
OORUVZHYQGKOFLPT
IHRINXEFEUYJAWTI
GOESBKYBBJNPLITV
CQVAYKISVEZOPTVL
WTNTOVCAGXHPBTUK
HDQHKMYXVHQICSFO
JOMBSGKIYRUTQBDB
GBDWIISECOAKZUNR"""

#Nachfolgend hast du eine Liste mit einzelnen IDs, welche folgende Spezialitäten enthalten können:

#Ein bestimmter Buchstabe erscheint zwei Mal
#Ein bestimmter Buchstabe erscheint drei Mal
#Nachfolgend einige Beispiele dazu:

#"abcdef" # hat keine Spezialität
#"bababc" # Hat zweimal ein 'a' und dreimal ein 'b', womit beide Spezialitäten erscheinen
#"abbcde" # Hat zweimal ein 'b', womit nur die erste Spezialität erscheint
#"abcccd" # hat dreimal ein 'c', womit nur die zweite Spezialität erscheint
#"aabcdd" # Hat sowohl zweimal ein 'a' als auch zweimal ein 'b'. Zählt als *einmal* die erste Spezialität
#"abcdee" # Hat zweimal ein 'e', erste Spezialität
#"ababab" # Hat dreimal ein 'a' und 'b', zählt als *einmal* die zweite Spezialität
#Summiere die Anzahl der jeweiligen Erscheinungen der Spezialitäten.. Bei den oberen Beispielen wäre dies also 4-mal die erste Spezialität und 3-mal die zweite Spezialität. Diese beiden Zahlen gibt es zu multiplizieren und die Lösung für dieses Beispiel ist:

#4 * 3 = 12
#Hinweis: die count Methode einer Liste könnte Hilfreich sein:

#list("aabbcc").count("a") # resultiert 2
#list("aaabbcc").count("a") # resultiert 3
#list("AABBCC").count("a") # resultiert in 0
#Berechne nun dieses spezielle Produkt für folgende ID's. Die richtige Lösung erkennst du daran, dass sie ein vielfaches von 111 ist.

# count the lines 
lines=ids.count("\n") + 1

#split ids read out string as a list
listed = ids.split("\n")

#counter
sum_2 = 0
sum_3 = 0

#repeat this thing for every line(50x) 
for i in range(lines):
    # for every character in element of the list check this:
    for character in listed[i]:
        # check if when characters are counted any character apears 3 times
        if listed[i].count(character) == 3:
            #update counter (divide by amount of characters)
            sum_3 +=1/3
        if listed[i].count(character) == 2:
            sum_2 +=1/2

#spit it
print(int(sum_2), "*", int(sum_3+1), "=",int(sum_2)*int(sum_3+1) )







