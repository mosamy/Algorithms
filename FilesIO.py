

import binascii
from itertools import cycle, izip

my_file = open("Mawlana.jpg", "rb")

# Add your code below!
f = my_file.read()
text = binascii.hexlify(f)
key = 's3cr3t'
print 'f'
print f

print text
textcyph = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(f, cycle(key)))

print 'textcyph'
print textcyph

# write cyph

writefile = open("CyphMawlana.jpg", "wb")
writefile.write(textcyph)
writefile.close()

textuncyph = ''.join(chr(ord(c)^ord(k)) for c, k in izip(textcyph, cycle(key)))
print 'textuncyph'
print textuncyph

writefile = open("unCyphMawlana.jpg", "wb")
writefile.write(textuncyph)
writefile.close()

#print f

# <editor-fold desc="Description">
# text = binascii.hexlify(f)
# print text
#
# key = 's3cr3t'
# textcyph= ''.join(chr(ord(c)^ord(k)) for c, k in izip(text, cycle(key)))
# textuncyph = ''.join(chr(ord(c)^ord(k)) for c, k in izip(textcyph, cycle(key)))
#
# print ('text Cypher')
# print(textcyph)
#
#
# #TypeError: Non-hexadecimal digit found
# #print binascii.a2b_hex(textcyph)
# print ('text deCypher')
# print(textuncyph)
#
# print "Hex coming"
# print binascii.a2b_hex(textuncyph)
# my_file.close()
# #for itm in my_list:
# #    my_file.write(str(itm))
# #    my_file.write("\n")
# #my_file.close()
# # </editor-fold>
