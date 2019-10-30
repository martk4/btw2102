#Schreibe eine Methode mit dem Namen smart_area, welche drei Named-Parameter hat: width, height und shape. Die ersten zwei Parameter sind selbsterklärend. Der Dritte akzeptiert folgende Werte: square, rectangle und triangle. Auch ist square der Standardwert von shape.

#Bei square sollst Du die Fläche eines Quadrates berechnen. Dazu ist nur der Parameter width involviert, da die Seitenlängen gleich sind.

#Bei rectangle sollst Du die Fläche eines Rechtecks berechnen. Dazu braucht es eine Breite und die Höhe (width und height).

#Bei triangle sollst Du die Fläce eines Dreiecks berechnen. Dazu braucht es eine Breite und die Höhe (width und height).

#Werden unlogische Argumente übergeben (z.B. keine Höhe für ein Dreieck), gelten alle Argumente als invalid und die Funktion soll -1 als Fläche zurückgeben.

def smart_area(width=None,height=None,shape="square"):
    if shape == "invalid":
        return -1
    if width is not None and height is not None and shape is not "triangle":
        if width < 0 or height < 0:
            return -1
        else:
            return width*height
    if shape == "square":
        if width < 0:
            return -1
        else:
            return width**2
    if shape == "rectangle":
        if height is None :
            return -1
        else :
            return width*height
    if shape == "triangle":
        if height is None :
            return -1
        else:
            return width*height/2
    else:
        return -1


#Beispiele:

#smart_area(3) # results in 9 (square)
#smart_area(width=3, height=4, shape='triangle') # results in 6
#smart_area(3, 4, 'rectangle') # results in 12
#smart_area(width=1, shape='triangle') # height is missing => -1
#Nachfolgenden Code kannst Du benutzen um Deine Lösung zu testen. Kopiere ihn ans Ende deines Scripts.

assert smart_area(width=2) == 4, "Square was not detected correctly"
assert smart_area(2, height=4) == 8, "Rectangle was not detected correctly."
assert smart_area(2, height=3, shape='triangle') == 3, "Triangle was not detected correctly."
assert smart_area(2, shape='triangle') == -1, "triangle without height is illegal"
assert smart_area(-1) == -1, "less than zero is invalid input"
assert smart_area(1, -1) == -1, "less than zero is invalid input"
assert smart_area(1, 2, 'invalid') == -1, "only square, rect and triangle are allowed"

print("Your 'smart_area'-function works flawlessly. Nice job!")