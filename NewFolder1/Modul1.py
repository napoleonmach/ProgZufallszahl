
Vorteile von funktionalen Programmiersprachen
	Funktionen als First-Class Citizens: Funktionen können in funktionalen Sprachen genauso behandelt werden wie Daten
	Rekursion statt Schleifen: Funktionale Programmierung bevorzugt rekursive Ansätze
	Deklarative Programmierung: Funktionalen Sprachen folgen oft einem deklarativen Ansatz im Gegensatz zu einem imperativen
	Nebenläufigkeit und Parallelität: Die Immutabilität von Daten in funktionalen Sprachen erleichtert die Behandlung von Nebenläufigkeit, da keine Sorge um Zustandsänderungen besteht
	Bessere Testbarkeit: Funktionen in funktionalen Sprachen sind oft leichter testbar
	Vermeidung von Null-Referenzen: Viele funktionale Sprachen bieten Mechanismen, um Null-Referenzen zu vermeiden, was zu sichererem Code führt.
	
	
        y_values = [reduce (expression) for x in x_values] // Vorlage:  result = reduce(function, sequence[, initial])


import random

def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)  # Zufällige x-Koordinate zwischen 0 und 1
        y = random.uniform(0, 1)  # Zufällige y-Koordinate zwischen 0 und 1

        # Überprüfen, ob der Punkt innerhalb des Viertelkreises liegt
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # Das Verhältnis der Punkte im Viertelkreis zu allen Punkten entspricht Pi/4
    return (points_inside_circle / num_points) * 4

# Anzahl der zufälligen Punkte
num_points = 100000

# Pi schätzen
estimated_pi = estimate_pi(num_points)

print(f"Geschätzte Pi: {estimated_pi}")

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

# Generiere und drucke die nächsten 5 Zufallszahlen
for _ in range(5):
    print(lcg.next())

Veränderung: Sinkende Bereitschaft der Mitarbeiterschaft. Fehlende Genauigkeit. 


Vielseitigkeit und Flexibilität: Verschiedene Probleme können effizienter mit unterschiedlichen Programmierparadigmen gelöst werden. Die Möglichkeit, mehrere Paradigmen zu unterstützen, ermöglicht es Entwicklern, das für die spezifische Aufgabe am besten geeignete Paradigma auszuwählen.

Wiederverwendung von Code: Ein Entwickler kann bestehenden Code in neuen Projekten wiederverwenden, selbst wenn diese Projekte unterschiedliche Paradigmen verwenden. Dies erleichtert die Code-Wiederverwendung und ermöglicht es, bewährte Lösungen aus verschiedenen Kontexten zu übernehmen.



1. Warum unterstützen die meisten in der Praxis verwendeten Programmiersprachen mehrere Programmierparadigmen? (maximal drei Sätze)

Integration von Bibliotheken und Frameworks: Viele Bibliotheken und Frameworks sind in einer bestimmten Programmiersprache für ein spezielles Paradigma entwickelt worden. Die Unterstützung mehrerer Paradigmen erleichtert die Integration dieser Tools in Projekte und ermöglicht Entwicklern den Zugriff auf eine breite Palette von Ressourcen.


1. Weshalb lassen sich rein funktional erstellte Programme gut parallelisieren? (maximal drei Sätze)

Rein funktionale Programme lassen sich gut parallelisieren, da sie keine gemeinsam genutzten Zustände oder Seiteneffekte haben. Die Unveränderlichkeit von Daten ermöglicht es, Funktionen unabhängig voneinander auszuführen, was die Parallelisierung erleichtert und die Gefahr von Datenkonflikten minimiert

