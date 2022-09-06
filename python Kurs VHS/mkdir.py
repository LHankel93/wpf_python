import os

try:
    pfad = 'C:/HalloWelt/'
    os.mkdir(pfad)
    print('mkdir ' + pfad + 'erfolgreich')
except:
    print(Fehler)
    