from pprint import pprint
import sys,json, importlib

class Runner:
    @classmethod
    def __init__(self):
        self.a = importlib.import_module("abuseipdb_package.abuseipdb").Abuseipdb()        
        self.f = importlib.import_module("forti_package.forti").Forti()
        self.h = importlib.import_module("helpers").Helpers()
    
    def file_input(self):
        self.h.clear()
        print("Please follow instruction below: ")
        print("1. Download a csv file from Intrusion Prevention menu in your FortiAnalyzer")
        print("2. Make sure your file are .csv with FortiAnalyzer formatted")
        print("3. Place your .csv file into /data/log/")
        print("\nUnderstand ?")
        choice = input("Your choice [y/n]: ")
        if choice == "y" or choice == "Y":
            if self.f.find_log() != False:
                self.f.extract_files()
                result = self.f.pretty_files()
                with open(result['json_path'], 'rb') as f:
                    array = json.load(f)
                    for x in range(len(array)):
                        srcip = array[x]['srcip']
                        self.a.check_report(srcip)  
                print("Check generated files on /data in case you need final csv and json files")      
                self.h.try_again()
            else:
                self.h.try_again()
        else:
            self.menu()


    def manual_input(self):
        loops = input("Total Attacker: ")
        inputs = [] #save to list 
        try:
            if loops.isdigit() and 1 <= int(loops) <= 7:
                print("User Input is valid.")
                for x in range(int(loops)): 
                    inputs.append(input("IP Address: ")) 
                    if self.h.is_valid_ipv4_address(inputs[x]) == True:
                        print("IP Address valid")
                        self.a.check_report(inputs)
                    else:
                        print("IP Address is not valid")
                        self.h.try_again()
                self.h.try_again()
            elif int(loops) > 7:
                print("Too much attacker, better using csv file.")
                self.h.try_again()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("User input is not valid")
            self.h.try_again()
    
    def bot_automation(self):
        print("Bot Automation is under construction")
        pass
        
    def menu(self):
        self.h.clear()
        print("Welcome to FARPA")
        print("Select menu:")
        print("1. File Input")
        print("2. Manual Input")
        print("3. Bot Automation")
        print("4. Credits")
        print("5. Exit")
        choice = input("Your choice [1-5]: ")
        if choice == "1":
            self.file_input()
        elif choice == "2":
            self.manual_input()
        elif choice == "3":
            self.h.clear()
            self.bot_automation()
            self.h.try_again()
        elif choice == "4":
            self.h.clear()
            self.h.credits_to()
            self.h.try_again()
        elif choice == "5":
            sys.exit()
        else:
            print("Wrong Choice")
            self.h.try_again()
        
    def main(self):
        self.menu()

shot = Runner()
shot.main()
