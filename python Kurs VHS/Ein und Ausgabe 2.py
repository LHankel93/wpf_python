#!/usr/bin/python3

print("Bitte geb hier jetzt Deinen Text ein:\n")
eingabe = input()
ausgabedatei = open("ausgabe.txt", "a")
ausgabedatei.write(eingabe)
ausgabedatei.write("\n")
ausgabedatei.close()