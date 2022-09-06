#!/usr/bin/python3

import pymysql

# Öffnen der Datenbankverbindung
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Datenbank-Cursor wird definiert
cursor = db.cursor()

# Das notwendige SQL-Statement wird zusammengesetzt
sql = "UPDATE ANGESTELLTE SET AGE = 22 WHERE NACHNAME = 'Müller'"
try:
   # Ausführen des SQL-Kommandos
   cursor.execute(sql)
   # Commit-Anweisung an die Datenbank senden
   db.commit()
except:
   # Rollback im Fehlerfall
   db.rollback()

# Datenbankverbindung wieder trennen
db.close()
