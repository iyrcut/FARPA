from os import system, name
import sys, importlib
import os, socket

class Helpers():

    def is_valid_ipv4_address(self, address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False
        return True
    
    def clear(self): 
        if name == 'nt': 
            _ = system('cls') #windows
        else: 
            _ = system('clear') #linux or mac
    
    def try_again(self):
        print("\nGo to menu ?")
        choice = input("Your choice [y/n]: ")
        if choice == "y" or choice == "Y":
            callRunner = importlib.import_module("runner").Runner()
            callRunner.menu()
        elif choice == "n" or choice == "N":
            print("Program Exit")
            sys.exit()
        else:
            print("Wrong choice")
            self.clear()
            self.try_again()

    
    def credits_to(self):
       print("Coder: iyrcut")
       print("FortiAnalyzer Report and Publish Abuser (FARPA)")
       print("Story behind this project open README.md")
       print("Made with love")