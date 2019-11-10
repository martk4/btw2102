import os
#Auf der ersten Zeile findest Du Spaltennamen. 
# Die relevanten Spalten (country, name, estimated_generation_gwh, u.ä.) 
# musst Du entsprechend ausfindig machen. 
# Finde nun abhängig von diesen Spalten alle Kraftwerke der Schweiz. 
# Danach sollst Du die Kraftwerke in 2 Kategorien aufteilen: 
# Kernkraftwerke und Sonstige. 
# Danach sollst Du die geschätzten Produktionsmengen in GWH pro Kategorie aufsummieren 
# und am Schluss einen Prozentsatz ausrechnen: 
# Wie viel Strom in der Schweiz wird mit Kernkraftwerken produziert?

#Zum Beispiel

#(Estimated) Generated power by nuclear: 12.34%
categories= []
final_dic= []
def read_csv(country= "Switzerland"):
    global categories
    plants_country = []
    f = open('Aufgaben/global_power_plant_database.csv', 'r', errors='replace')
    all_plants = f.read().split("\n")
    categories = all_plants[0]
    f.close()

    for i in range(len(all_plants)):
        theplant= all_plants[i].split(",")
        for a in range(len(theplant)):
            if theplant[a]== country:
                plants_country.append(theplant)

    return plants_country
def dicing(raw):
    cat = categories.split(",")
    for i in range(len(raw)):
        tempdic= {}
        for a in range(len(raw[i])):
            tempdic[cat[a]]= raw[i][a]
        final_dic.append(tempdic)
    return final_dic    
def sort_plant(all_p,source="Nuclear"):
    type1=[]
    type2= []
    for i in range(len(all_p)):
        if all_p[i]["primary_fuel"] == source:
                type1.append(all_p[i])
        else:
            type2.append(all_p[i])
    return [type1,type2]
def sum_plant(t):
    summe_t1 = 0
    summe_t2 = 0

    for a in t[0]:
        summe_t1 += float(a['capacity_mw'])
    for a in t[1]:
        summe_t2 += float(a['capacity_mw'])

    return [summe_t1,summe_t2]
def percent(x):
    p= x[0]/(x[0]+ x[1]) *100


    return  str(p)+" Percent" 



print(percent(sum_plant(sort_plant(dicing(read_csv())))))
