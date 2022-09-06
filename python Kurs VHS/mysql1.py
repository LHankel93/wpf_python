#!C:/Users/Lorenz/AppData/Local/Microsoft/WindowsApps/python.exe

import pymysql

# Öffnen der Datenbank-Verbindung
db = pymysql.connect("localhost","testuser","test123","TESTDB")

# Einen sogenannten Cursor für die Ausführung vorbereiten
cursor = db.cursor()

# Erstellen der Tabelle "Angestellte"
sql = """CREATE TABLE ANGESTELLTE (
    VORNAME CHAR(20) NOT NULL,
    NACHNAME CHAR(20),
    AGE INT,
    GESCHLECHT CHAR(1),
    EINKOMMEN FLOAT )"""
cursor.execute(sql)
# Die Datenbank-Verbindung wieder schließen
db.close()