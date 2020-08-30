import requests
import argparse
import sys

def get_request(url):
    r = requests.get(url)
    print(r.text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', type=str, metavar='', required=True, help='HTTP method to use', choices=['get','post'])
    parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='URL to send request')
    args = parser.parse_args()

    print(args.method)
    if(args.method == 'get'):
        get_request(args.url)

if __name__ == "__main__":
    main()

