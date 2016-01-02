
# BrutePy
Python Brute Force for Http Auth

BrutePy is a tool that can be used to Brute Force a target that requires HTTP Auth.


**Usage**

```
python Brute.py https://192.168.1.1 rockyou.txt admin --delay 3 --startat 5
```

```
E:\git\BrutePy>python Brute.py -h
usage: Brute.py [-h] [--delay DELAY] [--startat STARTAT]
                [--ignore-consecutive-empty IGNORE_CONSECUTIVE_EMPTY]
                target words user

HTTP Auth Brute Force Tool

positional arguments:
  target                The target URI. ex http://192.168.1.1
  words                 The wordlist to choose passwords from
  user                  The username to use

optional arguments:
  -h, --help            show this help message and exit
  --delay DELAY         Time in milliseconds between each request
  --startat STARTAT     Start at this line in the file
  --ignore-consecutive-empty IGNORE_CONSECUTIVE_EMPTY
                        Ignore this many consec. empty lines before exiting

```





> Written with [StackEdit](https://stackedit.io/).
