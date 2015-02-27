

import binascii
from itertools import cycle, izip

my_file = open("test.txt", "r+")

# Add your code below!
f = my_file.read()
text = binascii.hexlify(f)

key = 's3cr3t'
textcyph= ''.join(chr(ord(c)^ord(k)) for c, k in izip(text, cycle(key)))
textuncyph = ''.join(chr(ord(c)^ord(k)) for c, k in izip(textcyph, cycle(key)))

print(textcyph)


#TypeError: Non-hexadecimal digit found
#print binascii.a2b_hex(textcyph)
print(textuncyph)
print binascii.a2b_hex(textuncyph)
my_file.close()
#for itm in my_list:
#    my_file.write(str(itm))
#    my_file.write("\n")
#my_file.close()
