__author__ = 'mohamed'


my_file = open("Mawlana.jpg", "r")
my_file_enc = open("MawlanaEnc.jpg", "a+")





def writeEncrypted(f, R):
    try:
        byte = ord(f.read(8))
        while byte != "":

            byte = f.read(1)
            byte = bin(byte) ^ 0b1110
            R.write(bin(byte))
    finally:
        f.close()
        R.close()

writeEncrypted(my_file, my_file_enc)