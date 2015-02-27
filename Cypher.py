__author__ = 'mosamy'

# Stupid XOR demo
from itertools import cycle, izip
filei = open("test.txt")
message = str(filei.read())
filei.close()

#filecyph = open("Cyphered.txt")
#msgcyph = filecyph.read()
#filecyph.close()

key = 's3cr3t'

cyphered = ''.join(chr(ord(c)^ord(k)) for c, k in izip(message, cycle(key)))
uncyphered = ''.join(chr(ord(c)^ord(k)) for c, k in izip(cyphered, cycle(key)))



def cypheredfile(filename, secretmessage):
    f = open(filename, 'a')  # replace the mode


    f.write(secretmessage + '\n')
    f.close()
    return f

def uncypheredfile(filename, key):
    f = open(filename, 'r')  # replace the mode
    cyph = f.read()
    uncyph = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(cyph, cycle(key)))
    f.close()
    # Append name and email, each record should end with
    fileuncyph = open('uncyph' + filename, 'a')
    fileuncyph.write(uncyph +'\n')
    fileuncyph.close()
    return f

def cypherfile (sourcefile, destinationfile, secretkey):
    #read sourcefile uncyphered string
    fsource = open(sourcefile, 'r')
    uncyph = fsource.read()
    fsource.close()

    cypher = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(uncyph, cycle(secretkey)))

    #open destination and add the cypehered text
    fdestination = open(destinationfile, 'a+')
    fdestination.write(cypher)
    fdestination.close()
    print 'source file decyphered = ' + sourcefile + '  destination file cyphered = ' + destinationfile

def decypherfile(sourcefile, destinationfile, secretkey):
     #read sourcefile uncyphered string
    fsource = open(sourcefile, 'r')
    cypher = fsource.read()
    fsource.close()

    uncypher = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(uncyph, cycle(secretkey)))

    #open destination and add the uncypehered text
    fdestination = open(destinationfile, 'a+')
    fdestination.write(uncypher)
    fdestination.close()
    print 'source file cyphered = ' + sourcefile + '  destination file decyphered = ' + destinationfile



#secret = ('%s' % cyphered)
#cypheredfile('Cyphered.txt', secret)
#uncypheredfile('unCyphered.txt', key)

cypherfile('test.txt', 'cypheredtest.txt', 'N@zim')
decypherfile('cypheredtest.txt', 'decypheredtest.txt', 'N@zim')