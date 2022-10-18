# Passwortmanager für WPF Python Montag Lorenz Hankel FA-B-01

# Passwort Klasse definieren
from ast import Pass
from copy import deepcopy
import base64
from operator import index
import os
from pathlib import Path


class Passwort():
    def __init__(self, index:int , name:str, passwort:str, url:str, hinweis:str):
        self.index = index
        self.name = name
        self.passwort = passwort
        self.url = url
        self.hinweis = hinweis
    def set_index(self, index:int):
        self.index = index
    def set_name(self, name:str):
        self.name = name
    def set_passwort(self, passwort:str):
        self.passwort = passwort
    def set_url(self, url:str):
        self.url = url
    def set_hinweis(self, hinweis:str):
        self.hinweis = hinweis
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name
    def get_passwort(self):
        return self.passwort
    def get_url(self):
        return self.url
    def get_hinweis(self):
        return self.hinweis
    def __str__(self):
        sep = ":"
        return (f"{str(self.index) + sep + str(self.name) + sep + str(self.passwort) + sep + str(self.url) + sep + str(self.hinweis)}")
    def print_data(self):
        sep = "\t"
        print (f"{str(self.index) + sep + str(self.name) + sep + str(self.passwort) + sep + str(self.url) + sep + str(self.hinweis)}")

def master_Passwort_anlegen():
    # Neues Passwort vom Nutzer abfragen
    __pw = bytes(input("Bitte geben Sie das neue Master-Passwort an. Vergessen Sie es nicht!\n"), "utf-8")
    __pw_enc = base64.b64encode(__pw)
    # nun das verschlüsselte Passwort in Datei schreiben.
    datei = open("./Passwortmanager/login.txt", "w")
    datei.write((__pw_enc).decode("utf-8"))
    datei.close()

def ersteinrichtung(pw_liste):
    print("\nErsteinrichtung starten... \n")
    # Neues Master Passwort anlegen
    master_Passwort_anlegen()
    # Passwort Liste mit Test-Daten füllen
    Teste_Liste_erstellen()
    # Passwort Datei schreiben mit den angelegten Test-Daten
    Datei_Schreiben(pw_liste)
    Datei_Lesen(pw_liste)
    print("\nErsteinrichtung beendet. \n")

def master_Passwort_pruefen():
    datei = open("./Passwortmanager/login.txt", "r")
    __login = bytes(datei.read(), "utf-8")
    __pw = bytes(input("\nBitte geben Sie Ihr Master Passwort ein.\n"), "utf-8")
    if base64.b64decode(__login)!= __pw:
        print("Passwort ist falsch")
        exit()
    else :
        print("Zugangsdaten sind korrekt.")

def einrichtung_pruefen():
    __master_datei = Path("./Passwortmanager/login.txt")
    __passwort_datei = Path("./Passwortmanager/passwords.txt")
    if __master_datei.is_file() == False and __passwort_datei.is_file() == False:
        ersteinrichtung(pw_liste)
    elif __master_datei.is_file() and __passwort_datei.is_file() == False:
        print("\nMaster Login Datei fehlt. Setze Installation zurück.\n")
        os.remove("./Passwortmanager/login.txt")
        ersteinrichtung(pw_liste)
    else :
        print("\nSystem in Ordnung.\n")
        master_Passwort_pruefen()
        Datei_Lesen(pw_liste)

def datensatz_loeschen(pw_liste, index_loeschen:int):
    print("\nDS mit folgenden Index werden gesucht: " + str(index_loeschen) + "\n")
    vgl_liste = deepcopy(pw_liste) # zum Vergleichen später
    listen_index:int = -1
    count:int = 0
    for i in pw_liste:
        print(str("Aktueller Index zum Vergleich: " + Passwort.get_index(i)) + "\n")
        if int(Passwort.get_index(i)) == int(index_loeschen):
            print("\nFolgender DS wird gelöscht: " + str(index_loeschen) + "\n")
            listen_index = count
            break
        else: 
            count +=1
    if listen_index != -1:
        del(pw_liste[listen_index])
        Datei_Schreiben(pw_liste)
        Datei_Lesen(pw_liste)
        print("Es wurden " + str((int(len(vgl_liste)) - int(len(pw_liste)))) + " Elemente aus der Datenbank gelöscht.")
    else:
        print("Kein entsprechendes Element in der Datenbank gefunden")

def Datei_Lesen(pw_liste):
    datei = open("./Passwortmanager/passwords.txt", "r")
    count = 0
    Lines = datei.readlines()
    # Strips the newline character
    for line in Lines:
        count += 1
        pw_attribute = []
        pw_attribute = line.split(":")
        #for i in pw_attribute:
          #  print(i)
        pw = Passwort(pw_attribute[0], pw_attribute[1], pw_attribute[2], pw_attribute[3], pw_attribute[4])
        pw_liste.append(pw)
    datei.close

# Schreiben einer Passwort Datei
def Datei_Schreiben(pw_liste):
    datei = open("./Passwortmanager/passwords.txt", "w")
    for x in pw_liste:
        datei.write(str(x))
    datei.close

# Testet das Erstellen und füllen der Passwort Liste
def Teste_Liste_erstellen():
    for i in range(1,3):
        ein_Passwort = Passwort(i, "EinPasswortName", "Das Passwort", "Die URL", "Ein Hinweis")
        pw_liste.append(str(ein_Passwort) + "\n")

def Ausgabe_Pw_Liste(pw_liste):
    print("-------------------------------------------------------------------------------------")
    print("Index\tName\t\t\tPasswort\t\tURL\t\tHinweis")
    print("-------------------------------------------------------------------------------------")
    for i in pw_liste:
        index = Passwort.get_index(i)
        name = Passwort.get_name(i)
        passwort = Passwort.get_passwort(i)
        url = Passwort.get_url(i)
        hinweis = Passwort.get_hinweis(i)
        print(index + "\t" + name + "\t\t" + passwort + "\t\t" + url + "\t\t" + hinweis)

def finde_naechsten_index():
    # liste mit allen Indezes anlegen
    index_list = []
    for i in pw_liste:
        index_list.append(Passwort.get_index(i))
    # Liste sortieren um Maximum zu finden
    index_list.sort()
    next_index:int = int(index_list[-1]) + 1
    return next_index


def neuen_Datensatz_anlegen():
    index:int = finde_naechsten_index()
    name:str = str(input("Geben Sie Ihren Accountnamen für den neuen Datensatz ein.\n"))
    passwort:str = str(input("Geben Sie Ihr Passwort für den neuen Datensatz ein.\n"))
    url:str = str(input("Geben Sie die URL für den neuen Datensatz ein.\n"))
    hinweis:str = str(input("(optional) Geben Sie einen Hinweis für den neuen Datensatz ein.\n"))
    if hinweis == "":
        hinweis = " "
    ein_Passwort = Passwort(index, name, passwort, url, hinweis)
    pw_liste.append(str(ein_Passwort) + "\n")
    Datei_Schreiben(pw_liste)
    Datei_Lesen(pw_liste)

def auswahl_Menue(pw_liste):
    print("1) Zeige existierende Passwörter")
    print("2) Füge ein neues Passwort hinzu")
    print("3) Lösche ein Passwort")
    print("4) Aktualisiere Passwort")
    print("5) Beende\n")
    auswahl:int = 0
    while auswahl < 1 or auswahl > 5:
        auswahl:int = int(input())
    match auswahl:
        # Liste ausgeben
        case 1:
            Ausgabe_Pw_Liste(pw_liste)
        # Neuen Datensatz anlegen
        case 2:
            neuen_Datensatz_anlegen()
        # Lösche einen Datensatz
        case 3:
            #TODO: Löschen eines DS
            datensatz_loeschen(pw_liste, int(input("\nBitte geben Sie den Index des zu löschenden Passwortes ein.\n")))
        # Ändere einen Datensatz
        case 4:
            #TODO: Ändern eines DS
            pass
        # Beenden
        case 5:
            exit()

# Oben Methoden / Funktionen
# --------------------------------------------------------------------------------------
# Unten Logik / Ablauf Planung

# Liste für Passwörter definieren
pw_liste = []
# Prüfen der Umgebung
einrichtung_pruefen()
# Ausgabe der formatierten Daten aus der Passwort Datei.
Ausgabe_Pw_Liste(pw_liste)
while True:
    auswahl_Menue(pw_liste)