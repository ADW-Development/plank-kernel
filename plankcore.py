# System

import importlib.util
import os

def load_interface():
    global Cli

    interface_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "interface.py")

    if os.path.exists(interface_path):
        spec = importlib.util.spec_from_file_location("interface", interface_path)
        interface = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(interface)
        Cli = interface.Cli
    else:
        print("interface.py not found!")

class Core:
    def Resetsystem():
        Bootmgr_Test_Resp = 0
        Utils_Test_Resp = 0

class Utils:
    def Panic(PanicCode):        
        Critical.Outp(f"[ SYS PANIC - {PanicCode} ]")
        Critical.Outp("Please insure system is installed correctly.")
    
    def Test():
        global Utils_Test_Resp
        Utils_Test_Resp = 1

class Bootmgr:
    def Test():
        global Bootmgr_Test_Resp
        Bootmgr_Test_Resp = 1 # If this is working properly, it will set the request to 1, else it will remain 0.
    
    def Boot():
        load_interface()
        Decoration.Banner()
        Core.Resetsystem()
        Critical.Outp("Welcome to Plank kernel.")
        Critical.Test("Bootmgr")
        Critical.Test("Utils")
        Core.Resetsystem()
        Cli.Loop()

class Critical:
    def Outp(String):
        print(String)
    
    def Test(TestType):
        if TestType == "Bootmgr":
            Bootmgr.Test()
            Critical.Outp(f"Bootmgr activity test | Response: {Bootmgr_Test_Resp}")

        if TestType == "Utils":
            Utils.Test()
            Critical.Outp(f"Utils activity test | Response: {Utils_Test_Resp}")


class Decoration:
    def Banner():
        Critical.Outp("""
            -----------------------
           |                       |
           |                       |
           |                       |
           |      ADW Systems      |
           |                       |
           |                       |
           |                       |
            -----------------------
              """)
