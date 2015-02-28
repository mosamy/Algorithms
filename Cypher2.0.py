
__author__ = 'mosamy'

# XOR encrytpion demo
from itertools import cycle, izip

def cypher(source, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(source, cycle(key)))

def cydecy(sourcefile, destinationfile, func):
    key = 'N@zim'
    with open(sourcefile, "r") as source:
        text = source.read()
    cytext = func(text, key)

    with open(destinationfile, "a+") as destination:
        destination.write(cytext)


