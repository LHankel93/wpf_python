#!/usr/bin/python3

import os

datei_existiert = os.path.exists('ausgabe.txt')
if datei_existiert == False:
    print('datei existiert nicht')
else:
    print('Datei existiert')