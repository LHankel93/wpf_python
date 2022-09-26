# Lorenz Hankel Fahrkartenautomat aus Java
# Import der relevanten Module:
from time import *
zu_Zahlender_Betrag:float = float(input("Bitte den zu zahlenden Betrag (EURO) eingeben: (z.B. 3.22)"))
eingezahlter_Gesamtbetrag:float = float("0.0")
eingeworfene_Münze:float = float("0.0")
rückgabebetrag:float = float("0.0")
eingegebener_Betrag:float = float("0.0")

# Bezahlvorgang
# ---------------
while eingezahlter_Gesamtbetrag < zu_Zahlender_Betrag :
    zwischensumme:float = zu_Zahlender_Betrag - eingezahlter_Gesamtbetrag
    print("Noch zu zahlen: %.2f" % (zwischensumme))
    eingeworfene_Münze =  float(input("Eingabe (mind. 5Ct, höchstens 2 EURO): "))
    eingezahlter_Gesamtbetrag += eingeworfene_Münze
print("bezahlt.")

# Ausgabe des Fahrscheins
#-----------------------
print("\nFahrschein wird ausgegeben\n------------")
for i in range(0, 8) :
    print("=", end=" ")
    sleep(0.25)
# Rückgeldberechnung und Ausgabe des Geldes
# ---------------------------------------
rückgabebetrag = eingezahlter_Gesamtbetrag - zu_Zahlender_Betrag
print("Zurück zu zahlender Betrag des Automaten: %.2f EURO" %rückgabebetrag)

while rückgabebetrag >= 2.0:
    print("2 EURO")
    rückgabebetrag -= 2.0
while rückgabebetrag >= 1.0:
    print("1 EURO")
    rückgabebetrag -= 1.0
while rückgabebetrag >= 0.5:
    print("0,50 EURO")
    rückgabebetrag -= 0.5
while rückgabebetrag >= 0.2:
    print("0,2 EURO")
    rückgabebetrag -= 0.2
while rückgabebetrag >= 0.1:
    print("0,10 EURO")
    rückgabebetrag -= 0.1
while rückgabebetrag >= 0.05:
    print("0,05 EURO")
    rückgabebetrag -= 0.05
while rückgabebetrag >= 0.02:
    print("0,02 EURO")
    rückgabebetrag -= 0.02
while rückgabebetrag >= 0.01:
    print("0.01 EURO")
    rückgabebetrag -= 0.01
print("\nVergessen Sie nicht, den Fahrschein\n vor Fahrtantritt entwerten zu lassen!\nWir Wünschen Ihnen eine gute Fahrt.")