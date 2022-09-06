#!/usr/bin/python3

import pymysql

# Datenbankverbindung öffnen
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Definition des DB-Cursors
cursor = db.cursor()

# Zusammenstellung des SQL-Statements
sql = "DELETE FROM ANGESTELLTE WHERE NACHNAME = 'Müller'"
try:
   # Ausführen des SQL-Kommandos
   cursor.execute(sql)
   # Commit an die DB senden
   db.commit()
except:
   # Rollback im Fehlerfall
   db.rollback()

# Datenbankverbindung wieder trennen
db.close()
