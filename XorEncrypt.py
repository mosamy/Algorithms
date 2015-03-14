__author__ = 'mosamy'
#
# NB : this is not secure
# from http://code.activestate.com/recipes/266586-simple-xor-keyword-encryption/
# added base64 encoding for simple querystring :)
#
from itertools import izip, cycle
import base64


def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored


secret_data = "Hello"
print xor_crypt_string(secret_data, encode=True)
print xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True)