__author__ = 'mosamy'

# Stupid XOR demo
from itertools import cycle, izip
filei = open("test.txt")
message = str(filei.read())
filei.close()

key = 's3cr3t'

cyphered = ''.join(chr(ord(c)^ord(k)) for c, k in izip(message, cycle(key)))

def cypheredfile(filename, secretmessage):
    f = open(filename, 'w')  # replace the mode

    # Append name and email, each record should end with
    f.write(secretmessage +'\n')
    f.close()
    return f

secret = ('%s' % cyphered)
cypheredfile('Cyphered.txt', secret)

