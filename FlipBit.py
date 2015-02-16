__author__ = 'mosamy'
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = mask ^ number
    return bin(result)