__author__ = 'mosamy'

# XOR encrytpion demo
from itertools import cycle, izip


def cypherfile (sourcefile, destinationfile, secretkey):
    #read sourcefile uncyphered string
    fsource = open(sourcefile, 'r')
    uncyph = fsource.read()
    fsource.close()

    cypher = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(uncyph, cycle(secretkey)))

    #open destination and add the cypehered text
    fdestination = open(destinationfile, 'w+')
    fdestination.write(cypher)
    fdestination.close()
    print 'source file decyphered = ' + sourcefile + '  destination file cyphered = ' + destinationfile

def decypherfile(sourcefile, destinationfile, secretkey):
     #read sourcefile uncyphered string
    fsource = open(sourcefile, 'r')
    cypher = fsource.read()
    fsource.close()

    uncypher = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(cypher, cycle(secretkey)))

    #open destination and add the uncypehered text
    fdestination = open(destinationfile, 'w+')
    fdestination.write(uncypher)
    fdestination.close()
    print 'source file cyphered = ' + sourcefile + '  destination file decyphered = ' + destinationfile


cypherfile('test.txt', 'cypheredtest.txt', 'N@zim')
decypherfile('cypheredtest.txt', 'decypheredtest.txt', 'N@zim')