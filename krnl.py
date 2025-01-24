# The system kernel

import importlib.util
import os

plankcore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plankcore.py")

if os.path.exists(plankcore_path):
    spec = importlib.util.spec_from_file_location("plankcore", plankcore_path)
    plankcore = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plankcore)
    Bootmgr = plankcore.Bootmgr
else:
    print("plankcore.py not found!")

Bootmgr.Boot()
