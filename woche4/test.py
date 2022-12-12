class Fahrzeug:
    __zaehler = 0
    
    def __init__(self):
        type(self).__zaehler += 1

    # Mit dem übergebenen self wird immer das übergebene Objekt self benötigt um die Methode abzufragen.
    def AnzahlFahrzeuge(self):
        return Fahrzeug.__zaehler
    
x = Fahrzeug()
print(x.AnzahlFahrzeuge())
y = Fahrzeug()
print(y.AnzahlFahrzeuge())

class Fahrzeug:
    __zaehler = 0
    
    def __init__(self):
        type(self).__zaehler += 1

    # Ohne Self nicht mehr statisch und man kann außerhalb eines Objektes der Klasse darauf zugreifen.
    @staticmethod #ermöglicht unabhängiges Abfragen derselben Methode.
    def AnzahlFahrzeuge():
        return Fahrzeug.__zaehler
    
    #Als Alternative eine Klassenmethode
    @classmethod
    def Anzahlfahrzeuge(cls):
        return cls, Fahrzeug.__zaehler


print(Fahrzeug.AnzahlFahrzeuge())