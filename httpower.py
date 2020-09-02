import requests
import argparse
import sys

#Parse user input 

cookiejar = requests.cookies.RequestsCookieJar()
postdata = {}
headers = ''

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--method', type=str, metavar='', required=True, help='HTTP method to use', choices=['get','post'])
parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='URL to send request')
    
parser.add_argument('-p', '--proxy', type=str, metavar='', help='Specify proxy to send request through')
parser.add_argument('-d', '--data', type=str, metavar='', help="Data to be sent for POST and PUT requests")    
parser.add_argument('-c', '--cookie', type=str, metavar='', help="Specify cookie values")    
parser.add_argument('-t', '--timeout', type=int, metavar='', default=3, help="Timeout in seconds to wait for response") 
parser.add_argument('-g', '--generate', action='store_true', help='Only generate the html of the request')

noise = parser.add_mutually_exclusive_group()
noise.add_argument('-v', '--verbose', action='store_true', help='Increase verbosity')
noise.add_argument('-q', '--quiet', action='store_true', help='Decrease verbosity')

args = parser.parse_args()

def format_request(r):
    
    #extract path from url
    loc = '/' + args.url.split('/', 3)[3]
    print(r.request.method + ' ' + loc + ' HTTP/1.1')
    
    #print out all of the headers
    for header,value in r.request.headers.items():
        print(header + ': ' + value)
    
    #print out the data sent to server if posting
    if (args.method != 'get'):
        print('\n' + r.request.body)

def format_response(r):
    
    #get common status code information
    status = ''
    if r.status_code == 200:
        status = 'OK'
    if r.status_code == 301:
        status = 'MOVED PERMANENTLY'
    if r.status_code == 302:
        status = 'FOUND'
    if r.status_code == 307:
        status = 'TEMPORARY REDIRECT'
    if r.status_code == 400:
        status = 'BAD REQUEST'
    if r.status_code == 401:
        status = 'UNAUTHORIZED'
    if r.status_code == 403:
        status = 'FORBIDDEN'
    if r.status_code == 404:
        status = 'NOT FOUND'
    if r.status_code == 405:
        status = 'METHOD NOT ALLOWED'
    if r.status_code == 500:
        status = 'INTERNAL SERVER ERROR'
    
    #print headers
    print('HTTP/1.1 ' + str(r.status_code) + ' ' + status)
    for header,value in r.headers.items():
        print(header + ': ' + value)

    #print response content
    print('\n' + r.content)


def get_request(url):
    try:

        #check for proxy and cookies
        if args.proxy: 
            if args.cookie: 
                r = requests.get(url,timeout=args.timeout,proxies=args.proxy,verify=False,cookies=cookiejar)
            else: 
                r = requests.get(url,timeout=args.timeout,proxies=args.proxy,verify=False)
        else:
            if args.cookie: 
                r = requests.get(url,timeout=args.timeout,cookies=cookiejar)
            else: 
                r = requests.get(url,timeout=args.timeout)

        #possible error in format? maybe timeout?
    except:
        print('\n[-] Error getting HTTP response. Make sure there are no syntax errors in supplied input.\n')
        sys.exit(1)

    if not args.quiet:
        if args.verbose:
            print('\n[+] CONTENT SENT\n')
            format_request(r)
        print('\n[+] SERVER RESPONSE\n')
        format_response(r)
            

def post_request(url, data):
    try:

        #check for proxy and cookies
        if args.proxy: 
            if args.cookie: 
                r = requests.post(url,data=data,timeout=args.timeout,proxies=args.proxy,verify=False,cookies=cookiejar)
            else: 
                r = requests.post(url,data=data,timeout=args.timeout,proxies=args.proxy,verify=False)
        else:
            if args.cookie: 
                r = requests.post(url,data=data,timeout=args.timeout,cookies=cookiejar)
            else: 
                r = requests.post(url,data=data,timeout=args.timeout)

        #possible error in format? maybe timeout?
    except:
        print('\n[-] Error getting HTTP response. Check timeout and make sure there are no syntax errors in supplied input.\n')
        sys.exit(1)
    
    if not args.quiet:
        if args.verbose:
            print('\n[+] CONTENT SENT\n')
            format_request(r)
        print('\n[+] SERVER RESPONSE\n')
        format_response(r)

#check for errors in user input
def check_formatting():
    if args.method == 'post' and not args.data:
        print('\n[-] data must be supplied when using a POST method\n')
        parser.print_help()
        sys.exit(1)
    
    #if any cookies exist, format them and put them in the cookiejar
    if(args.cookie):
        cookies = args.cookie.replace(' ', '').split(',')  
        
        for cookie in cookies:
            cookie = cookie.split('=')
            try:
                cookiejar.set(cookie[0], cookie[1], domain=args.url.split('/',3)[2], path='/'+ args.url.split('/',3)[3])
            except:
                print('\n[-] error in cookie formatting. Ex: <field>=<value>,<field>=<value>,...\n')
                sys.exit(1)
    
    #if any post data exist, format and put into dictionary
    if(args.data):
        data = args.data.replace(' ', '').split(',')
    
        for entry in data:
            entry = entry.split('=')
            try:
                postdata[entry[0]] = entry[1]
            except:
                print('\n[-] error in post data formatting. Ex: <field>=<value>,<field>=<value>,...\n')
                sys.exit(1)

def main():
    
    #format data recieved
    check_formatting()
    
    #check for proxy
    if(args.proxy):
        args.proxy = { "http" : args.proxy,
                       "https" : args.proxy.replace('http','http')
                     } 

    #execute the appropriate http method
    if(args.method == 'get'):
        get_request(args.url)

    if(args.method == 'post'):
        post_request(args.url, postdata)

#run program
if __name__ == "__main__":
    main()

