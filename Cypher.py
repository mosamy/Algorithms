__author__ = 'mosamy'

# Stupid XOR demo
from itertools import cycle, izip
filei = open("test.txt")
message = str(filei.read())
filei.close()

filecyph = open("Cyphered.txt")
msgcyph = filecyph.read()
filecyph.close()

key = 's3cr3t'

cyphered = ''.join(chr(ord(c)^ord(k)) for c, k in izip(message, cycle(key)))
uncyphered = ''.join(chr(ord(c)^ord(k)) for c, k in izip(msgcyph, cycle(key)))


def cypheredfile(filename, secretmessage):
    f = open(filename, 'w')  # replace the mode

    # Append name and email, each record should end with
    f.write(secretmessage +'\n')
    f.close()
    return f

def uncypheredfile(filename, key):
    f = open(filename, 'r+')  # replace the mode
    cyph = f.read()
    uncyph = ''.join(chr(ord(c)^ord(k)) for c, k in izip(cyph, cycle(key)))
    f.close()
    # Append name and email, each record should end with
    fileuncyph = open('uncyph' +filename , 'a')
    fileuncyph.write(uncyph +'\n')
    fileuncyph.close()
    return f

secret = ('%s' % cyphered)
cypheredfile('Cyphered.txt', secret)
uncypheredfile('Cyphered.txt', key)

