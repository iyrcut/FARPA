import pandas
import csv, json
import glob, gzip, shutil
import sys, os, re
from os.path import abspath

class Forti:
    @classmethod
    def __init__(self):
        self.log_dir = os.path.abspath(__file__ + "/../../../data/log/")
        self.csv_dir = os.path.abspath(__file__ + "/../../../data/csv/")
        self.json_dir = os.path.abspath(__file__ + "/../../../data/json/")

    def find_log(self):
        print("Finding newest log ..")
        try:
            path = os.path.join(self.log_dir, '*.csv.log.gz')
            newest_log = max(glob.glob(path), key=os.path.getmtime)
            print("Log found")
            file_name = os.path.split(newest_log)[1]
            name_split = file_name.rsplit('.', 3)
            name_only = name_split[0]
            data = {"newest_log": newest_log, "file_name": file_name, "name_only": name_only}
            if len(data) == 3:
                print("Log valid")
                return data
            else:
                print("Something missing.. log is not valid or data is empty")
                return False
        except:
            print("Log is not found")
            print("Unexpected error:", sys.exc_info()[0])
            return False

    def extract_files(self):
        print("Extracting files ..")
        file_name = self.find_log()
        with gzip.open(file_name['newest_log'], 'rb') as f_in:
            with open(file_name['newest_log'].rsplit('.', 2)[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                

    def pretty_files(self):
        new_log = self.find_log()
        csv_path = os.path.join(self.csv_dir, new_log['name_only']+'-pretty.csv')
        json_path = os.path.join(self.json_dir, new_log['name_only']+'-pretty.json')
        df = pandas.read_csv(new_log['newest_log'].rsplit('.', 2)[0], header=None)  # read
        # s = df.sample()
        # a = s.replace(r"^(?!\w+\=).*", 'sdfsg', regex=True)  # edit & delete
        # b = s.replace(r"\w+\=", '', regex=True)  # edit & delete
        with open(new_log['newest_log'].rsplit('.', 2)[0], newline='') as f:
            reader = csv.reader(f)
            row1 = next(reader) 
            regex = r'\=(.*?)\''
            subst = "'"
            result = re.sub(regex, subst, str(row1)) #return string on list form
        
        #convert result to list algorithm
        a = str(result)[1:-1] #remove 1st beginning character and 1st ending character
        b = a.replace('\'',"") #remove apostrophe
        c = b.split(', ') #split character by comma, so it turn to list mode
        ##end convert result
        
        df.columns = c
        df.replace(r"\w+\=", '', regex=True, inplace=True)  # edit & delete
        df.to_csv(csv_path, index=False)  # export
        df.to_json(json_path, orient="records", indent=4)  # export
        data = {'csv_path':csv_path,'json_path':json_path}
        return data

