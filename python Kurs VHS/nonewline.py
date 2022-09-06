#!/usr/bin/python3

#importiere sys Modul damit ich das Skript beenden kann am Ende.
import sys, os

#Array erstellen und füllen
liste = ["Auto", "Schiff", "Flugzeug"]

#For Schleife, welche die Inhalte im Array mit Zeilenumbruch ausgibt.
for zeile in liste:
    print(zeile, "\r")

print('----')

#For Schleife, welche die Inhalte des Arrays nebeneinander ausgibt.
for i in range(3):
    print(liste[i], end = " ")

print()

#Beenden des Progamms über Sys Modul
sys.exit()

#Alternativ kann man auch mit dem OS Modul beenden wie folgt: (unsauber)
#os._exit(0)

#Ansonsten geht auch: (beendet das Backend)
#raise SystemExit
