#!/usr/bin/python3

import os
import time

kommando = 'wmic logicaldisk get deviceid'
os.system(kommando)
time.sleep(20)
