
# BrutePy
Python Brute Force for Http Auth

BrutePy is a tool that can be used to Brute Force a target that requires HTTP Auth.


**Usage**

```
$ python Brute.py -h
usage: Brute.py [-h] [--delay DELAY] [--startat STARTAT]
               --target --words --user

HTTP Auth Brute Force Tool

positional arguments:
  --target           The target URI. ex http://192.168.1.1
  --words            The wordlist to choose passwords from
  --user             The username to use

optional arguments:
  -h, --help         show this help message and exit
  --delay DELAY      Time in milliseconds between each request
  --startat STARTAT  Start at this line in the file
```

Currently BrutePy targets 192.168.1.1 statically.

Some things I'd like to do:

 1. Implement argparse
 2. Allow passing in of target
 3. Allow configurable delay

> Written with [StackEdit](https://stackedit.io/).
