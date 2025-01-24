import imp
import os

plankcore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plankcore.py")

if os.path.exists(plankcore_path):
    plankcore = imp.load_source('plankcore', plankcore_path)
else:
    print("plankcore.py not found!")

Critical = plankcore.Critical
Utils = plankcore.Utils

class Cli:
    def Loop():
        Cli.Input()
        Cli.Processcommand()
    
    def Input():
        global Command
        Command = input("Plank$>")
    
    def Processcommand():
        if Command == "help":
            Commands.help()
        
        if Command == "info":
            Commands.info()
        
        if Command == "Force_Panic":
            Commands.Force_Panic()

class Commands:
    def help():
        Critical.Outp("help")
        Critical.Outp("info")
    
    def info():
        Critical.Outp("System: Plank kernel")
        Critical.Outp("Software Manufacturer: ADW Systems")
        Critical.Outp("Version: Beta 0.1.0")
    
    def Force_Panic():
        Utils.Panic("User_Forced_Panic")
