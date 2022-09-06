#!/usr/bin/python3

import pymysql

# Öffnen der Datenbankverbindung
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Deklaration des Datenbank-Cursors
cursor = db.cursor()

# Zusammenstellen der SQL-Query
#sql = "SELECT * FROM ANGESTELLTE \
# WHERE EINKOMMEN > '%d'" % (1000)
sql = "SELECT * FROM ANGESTELLTE WHERE EINKOMMEN > 1000;"
try:
    # Ausführen des SQL-Statements
    cursor.execute(sql)
    # Alle Zeilen werden als Liste in einer Liste abgefangen
    ergebnisse = cursor.fetchall()
    for zeile in ergebnisse:
        vname = zeile[0]
        nname = zeile[1]
        age = zeile[2]
        geschlecht = zeile[3]
        einkommen = zeile[4]
     # Ausgabe der abgefangenen Ergebnisse
    print ("vname = %s,nname = %s,age = %d,geschlecht = %s,einkommen = %d" % \
    (vname, nname, age, geschlecht, einkommen ))
except:
    print("Fehler: Konnte die Daten nicht abfragen")
    # DB-Verbindung trennen
db.close()