import requests
import json
import sys

class Abuseipdb:
    @classmethod
    def __init__(self):
        self.api_key = "" #Your API key goes here

    def check_abuseipdb(self, srcip):
        url = 'https://api.abuseipdb.com/api/v2/check'
        querystring = {
            'ipAddress': srcip,
            'maxAgeInDays': '90'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.api_key
        }
        response = requests.request(
            method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)
        return decodedResponse

    def report_abuseipdb(self, newip):
        url = 'https://api.abuseipdb.com/api/v2/report'
        params = {
            'ip': newip,
            'categories': '14,15,19',
            'comment': 'Unauthorized connection attempt: bot, scanning, hacking'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.api_key
        }
        response = requests.request(
            method='POST', url=url, headers=headers, params=params)
        decodedResponse = json.loads(response.text)
        x = json.dumps(decodedResponse, sort_keys=True,
                       indent=4)
        return x
    
    def check_report(self, ipaddr):
        try:
            x = self.check_abuseipdb(ipaddr)
            newip = x['data']['ipAddress']
            score = x['data']['abuseConfidenceScore']
            if 10 <= score <= 80:
                print("Total score for %s is %s. This IP has been reported to abuseipdb.com" %
                        (newip, score))
                print(self.report_abuseipdb(newip))
            else:
                print("Total score for %s is %s. Total score is too high. This IP will not be report" % (
                    newip, score))
        
        except KeyError:
            print("Please register to abuseipdb.com to get your API key")
            print("Program Exit")
            sys.exit()

        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Program Exit")
            sys.exit()
        
        