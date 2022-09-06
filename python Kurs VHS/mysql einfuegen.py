#!/usr/bin/python3
import pymysql

# Öffnen der Datenbankverbindung
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Vorbereitung des Ausführungs-Cursors
cursor = db.cursor()

# Zusammenstellung der SQL-Query
sql = """INSERT INTO ANGESTELLTE(VORNAME,
NACHNAME, AGE, GESCHLECHT, EINKOMMEN)
VALUES ('Peter', 'Müller', 33, 'm', 2300)"""
try:
# Absetzen des SQL-Querys
    cursor.execute(sql)
# "Schreib-Änderungen" benötigen ein Commit!
    db.commit()
except:
# "Rollback" im Fehlerfall
    db.rollback()
# Trennen der Datenbankverbindung
    db.close()