
__author__ = 'mohamed'

#array stats

def queerElement(my_list):
    avg = average(my_list)
    queer = 0
    diff = 0
    diffelement = 0
    for element in my_list:
        diffelement  = abs(abs(element) - abs(avg))
        if diffelement > diff:
            queer = element
            diff = diffelement
    return queer 


def average(my_list):
    
    if len(my_list) > 0:
        sumlist = 0
        for x in range(0, len(my_list)):
            sumlist += my_list[x]

        return sumlist / len(my_list)
    else:
        return -1


def main():
    my_list = [7, 2, 150, 6, 5, 1, 29, 6, 4, 19, 11,-200]
    
    print("Average of list is: %d " % average(my_list))
    print('Queer element is: %d' % queerElement(my_list))
 # Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
