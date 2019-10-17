#Du hast eine Liste von Teilnehmer an einem Rennen. Pro Runde hat jeder Teilnehmer seine erreichte Zeit. Die einzelnen Runden sind als Liste vorhanden und die Zeit ist in Sekunden.

participants = [
    {
        "name": "seb",
        "times": [71, 69, 68, 67, 65, 65, 68, 72]
    },
    {
        "name": "max",
        "times": [77, 71, 69, 69, 67, 68, 68, 70]
    },
    {
        "name": "dani",
        "times": [70, 70, 70, 82, 69, 68, 68, 69]
    }
]
#In einem ersten Schritt sollst du das dict jedes Teilnehmers erweitern durch jeweils die schnellste und langsamste Runde. Wähle als Key einen Namen wie fastest und slowest.

#Danach finde die schnellste Runde von allen Teilnehmer übergreifend. Diese schnellste Zeit sollst Du um 20% erhöhen. Gibt es einen Teilnehmer der diese Zeit überschreitet mit seiner langsamsten Zeit, wird er disqualifiziert.

#Liste nun alle Teilnehmer mit ihren schnellsten Rundenzeit. Die disqualifizierten Teilnehmer sollen entsprechend bemerkt werden. Die Summe der schnellsten Rundenzeiten aller qualifizierten Teilnehmer ist 132.

#Beispiel aus erfunden Daten:

#liz disqualified
#theo quickest lap 72
#alex quickest lap 71
#Sum of fastets laps: 143