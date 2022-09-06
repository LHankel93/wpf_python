#!/usr/bin/python3

import os
pfad = 'C:/Windows/system32/'
logdateien = os.listdir(pfad)
for zeile in logdateien:
    print(zeile)