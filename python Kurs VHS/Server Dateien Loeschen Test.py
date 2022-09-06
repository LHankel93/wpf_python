#!/usr/bin/env python
import os
from datetime import datetime, timedelta
import time

b = os.path.expanduser('C:/Users/Lorenz/Desktop/Test/')
for full in os.listdir(b):
    f = os.path.join(b, full)
    file_mtime = datetime.fromtimestamp(os.path.getmtime(f))
    max_mtime = datetime.now() - timedelta(seconds=60)

    if file_mtime < max_mtime:
        os.remove(f)