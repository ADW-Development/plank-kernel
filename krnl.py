# The system kernel

import imp
import os

plankcore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plankcore.py")

if os.path.exists(plankcore_path):
    plankcore = imp.load_source('plankcore', plankcore_path)
else:
    print("plankcore.py not found!")

Bootmgr = plankcore.Bootmgr

Bootmgr.Boot()
