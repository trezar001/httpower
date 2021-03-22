# httpower
## Description
A simple python tool for making HTTP requests without all the bloat. Currently supports GET and POST requests with support for additional methods coming in the future.

## Usage
```
usage: httpower.py [-h] -m  -u  [-p] [-d] [-c] [-t] [-g] [-v | -q]

optional arguments:
  -h, --help       show this help message and exit
  -m , --method    HTTP method to use
  -u , --url       URL to send request
  -p , --proxy     Specify proxy to send request through
  -d , --data      Data to be sent for POST and PUT requests
  -c , --cookie    Specify cookie values
  -t , --timeout   Timeout in seconds to wait for response
  -g, --generate   Only generate the html of the request
  -v, --verbose    Increase verbosity
  -q, --quiet      Decrease verbosity
```

## Installation
Navigate to directory of choice and download the neccessary files with the following command.
```
git clone https://github.com/trezar001/httpower.git
```
Use pip to install any missing dependencies.
```
pip install -r requirements.txt
```
