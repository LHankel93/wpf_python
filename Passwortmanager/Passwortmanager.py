# Passwortmanager für WPF Python Montag Lorenz Hankel FA-B-01

# Passwort Klasse definieren
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
        sep = ";"
        return (f"{str(self.index) + sep + str(self.name) + sep + str(self.passwort) + sep + str(self.url) + sep + str(self.hinweis)}")
    def printData(self):
        sep = "\t"
        print (f"{str(self.index) + sep + str(self.name) + sep + str(self.passwort) + sep + str(self.url) + sep + str(self.hinweis)}")

def Datei_Lesen(pw_liste):
    datei = open("passwords.txt", "r")
    count = 0
    Lines = datei.readlines()
    # Strips the newline character
    for line in Lines:
        count += 1
        pw_attribute = []
        pw_attribute = line.split(";")
        for i in pw_attribute:
            print(i)
        pw = Passwort(pw_attribute[0], pw_attribute[1], pw_attribute[2], pw_attribute[3], pw_attribute[4])
        pw_liste.append(pw)
    datei.close

# Schreiben einer Passwort Datei
def Datei_Schreiben(pw_liste):
    datei = open("passwords.txt", "w")
    for x in pw_liste:
        datei.write(str(x))
    datei.close

# Testet das Erstellen und füllen der Passwort Liste
def Teste_Liste_erstellen():
    for i in range(1,10):
        ein_Passwort = Passwort(i, "EinPasswortName", "Das Passwort", "Die URL", "Ein Hinweis")
       # print(ein_Passwort)
        pw_liste.append(str(ein_Passwort) + "\n")


# Oben Methoden / Funktionen
# --------------------------------------------------------------------------------------
# Unten Logik / Ablauf Planung


# Liste für Passwörter definieren
pw_liste = []

#Teste_Liste_erstellen()
#Datei_Schreiben(pw_liste)

# Einlesen der vorhanden Passwörter in Pw_liste
Teste_Liste_erstellen()
Datei_Schreiben(pw_liste)
Datei_Lesen(pw_liste)

for i in pw_liste:
    print(i)