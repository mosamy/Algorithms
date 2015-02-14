__author__ = 'mosamy'


def is_prime(x):
    for n in range(2, x-1):
        if x % n == 0:
            return False
    return True

x = int(raw_input("Please enter a number:"))  
print is_prime(x)