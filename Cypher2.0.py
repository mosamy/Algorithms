
__author__ = 'mosamy'

# XOR encrytpion demo
from itertools import cycle, izip

def cypher(source="", key=""):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(source, cycle(key)))

def cydecy(sourcefile, destinationfile, mykey):
    key = mykey
    with open(sourcefile, "rb") as source:
        text = source.read()


    with open(destinationfile, "wb") as destination:
        destination.write(cypher(text,mykey))


def main():
    cydecy("Mawlana.jpg", "Mawlana2.jpg",'N@zim')
    cydecy("Mawlana2.jpg", "Mawlana4.jpg",'N@zim')

if __name__ == '__main__':
    main()