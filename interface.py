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
        if Command == "help":
            Commands.Help()
        
        if Command == "info":
            Commands.Info()
        
        if Command == "force panic":
            Commands.Force_Panic()

        if Command == "program":
            Commands.Run_Program()

class Commands:
    def Help():
        load_core()
        Critical.Outp("Help")
        Critical.Outp("Info")
        Critical.Outp("Force Panic")
        Critical.Outp("Program")
    
    def Info():
        load_core()
        Critical.Outp("System: Plank kernel")
        Critical.Outp("Software Manufacturer: ADW Systems")
        Critical.Outp("Version: Beta 0.1.5")
    
    def Force_Panic():
        load_core()
        Utils.Panic("User_Forced_Panic")
        time.sleep(3)
        sys.exit()

    def Run_Program():
        InpProgram = input("Program name: ")
        current_dir = os.getcwd()
        interpreter_path = os.path.join(current_dir, "appdata", "sep", "interpreter.py")
        os.system(f"python {interpreter_path} \"{InpProgram}\"")
