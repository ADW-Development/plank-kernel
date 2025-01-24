import importlib.util
import os
import time
import sys

def load_core():
    global Critical
    global Utils

    plankcore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plankcore.py")

    if os.path.exists(plankcore_path):
        spec = importlib.util.spec_from_file_location("plankcore", plankcore_path)
        plankcore = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plankcore)
        Critical = plankcore.Critical
        Utils = plankcore.Utils
    else:
        print("plankcore.py not found!")

class Cli:
    def Loop():
        while True:
            Cli.Input()
            Cli.Processcommand()
    
    def Input():
        global Command
        Command = input("Plank$> ")
    
    def Processcommand():
        if Command == "Help":
            Commands.Help()
        
        if Command == "Info":
            Commands.Info()
        
        if Command == "Force Panic":
            Commands.Force_Panic()

class Commands:
    def Help():
        load_core()
        Critical.Outp("Help")
        Critical.Outp("Info")
        Critical.Outp("Force Panic")
    
    def Info():
        load_core()
        Critical.Outp("System: Plank kernel")
        Critical.Outp("Software Manufacturer: ADW Systems")
        Critical.Outp("Version: Beta 0.1.2")
    
    def Force_Panic():
        load_core()
        Utils.Panic("User_Forced_Panic")
        time.sleep(3)
        sys.exit()
