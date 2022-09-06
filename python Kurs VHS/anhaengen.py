#!/usr/bin/python3

liste = ['Katze', 'Hund', 'Vogel']
print(liste)
liste.append('Goldfisch')
print(liste)
liste1 = ['Maus', 'Ratte']
liste.extend(liste1)
print(liste)
liste2 = liste + liste1
print(liste2)
liste.sort()
liste1.sort()
print(liste)
print(liste2)