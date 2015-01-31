__author__ = 'mohamed'

from random import randint
count = 0
while count < 3:

    num = randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
