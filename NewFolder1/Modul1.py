
Vorteile von funktionalen Programmiersprachen
	Funktionen als First-Class Citizens: Funktionen k�nnen in funktionalen Sprachen genauso behandelt werden wie Daten
	Rekursion statt Schleifen: Funktionale Programmierung bevorzugt rekursive Ans�tze
	Deklarative Programmierung: Funktionalen Sprachen folgen oft einem deklarativen Ansatz im Gegensatz zu einem imperativen
	Nebenl�ufigkeit und Parallelit�t: Die Immutabilit�t von Daten in funktionalen Sprachen erleichtert die Behandlung von Nebenl�ufigkeit, da keine Sorge um Zustands�nderungen besteht
	Bessere Testbarkeit: Funktionen in funktionalen Sprachen sind oft leichter testbar
	Vermeidung von Null-Referenzen: Viele funktionale Sprachen bieten Mechanismen, um Null-Referenzen zu vermeiden, was zu sichererem Code f�hrt.
	
	
        y_values = [reduce (expression) for x in x_values] // Vorlage:  result = reduce(function, sequence[, initial])


import random

def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)  # Zuf�llige x-Koordinate zwischen 0 und 1
        y = random.uniform(0, 1)  # Zuf�llige y-Koordinate zwischen 0 und 1

        # �berpr�fen, ob der Punkt innerhalb des Viertelkreises liegt
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # Das Verh�ltnis der Punkte im Viertelkreis zu allen Punkten entspricht Pi/4
    return (points_inside_circle / num_points) * 4

# Anzahl der zuf�lligen Punkte
num_points = 100000

# Pi sch�tzen
estimated_pi = estimate_pi(num_points)

print(f"Gesch�tzte Pi: {estimated_pi}")

___________________________________________
class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

# Beispielverwendung
seed = 42
a = 1664525
c = 1013904223
m = 2**32

lcg = LinearCongruentialGenerator(seed, a, c, m)

# Generiere und drucke die n�chsten 5 Zufallszahlen
for _ in range(5):
    print(lcg.next())

Ver�nderung: Sinkende Bereitschaft der Mitarbeiterschaft. Fehlende Genauigkeit. 


Vielseitigkeit und Flexibilit�t: Verschiedene Probleme k�nnen effizienter mit unterschiedlichen Programmierparadigmen gel�st werden. Die M�glichkeit, mehrere Paradigmen zu unterst�tzen, erm�glicht es Entwicklern, das f�r die spezifische Aufgabe am besten geeignete Paradigma auszuw�hlen.

Wiederverwendung von Code: Ein Entwickler kann bestehenden Code in neuen Projekten wiederverwenden, selbst wenn diese Projekte unterschiedliche Paradigmen verwenden. Dies erleichtert die Code-Wiederverwendung und erm�glicht es, bew�hrte L�sungen aus verschiedenen Kontexten zu �bernehmen.



1. Warum unterst�tzen die meisten in der Praxis verwendeten Programmiersprachen mehrere Programmierparadigmen? (maximal drei S�tze)

Integration von Bibliotheken und Frameworks: Viele Bibliotheken und Frameworks sind in einer bestimmten Programmiersprache f�r ein spezielles Paradigma entwickelt worden. Die Unterst�tzung mehrerer Paradigmen erleichtert die Integration dieser Tools in Projekte und erm�glicht Entwicklern den Zugriff auf eine breite Palette von Ressourcen.


1. Weshalb lassen sich rein funktional erstellte Programme gut parallelisieren? (maximal drei S�tze)

Rein funktionale Programme lassen sich gut parallelisieren, da sie keine gemeinsam genutzten Zust�nde oder Seiteneffekte haben. Die Unver�nderlichkeit von Daten erm�glicht es, Funktionen unabh�ngig voneinander auszuf�hren, was die Parallelisierung erleichtert und die Gefahr von Datenkonflikten minimiert

