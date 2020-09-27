FortiAnalyzer Report and Publish Abuser
=======================================
FARPA was created to make every unauthorized connection attempt that has been detected by IPS such as FortiAnalyzer being reported to abuseipdb.com. AbuseIPDB is a project dedicated to helping systems administrators and webmasters check and report IP addresses that are involved in malicious activity such as spamming, hack attempts, DDoS attacks, etc. AbuseIPDB publish every IP that has been reported as bad activity.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement dependencies.

```bash
pip install -r requirements.txt
```

## Usage

Go to /src directory and open terminal
```bash
python3 runner.py
```
or if your system run python3 by default instead of python2
```bash
py runner.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)