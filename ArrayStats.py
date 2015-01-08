__author__ = 'mohamed'

#array stats


def average(my_list):
    if len(my_list) > 0:
        sumlist = 0
        for x in range(0, len(my_list)):
            sumlist += my_list[x]

        return sumlist / len(my_list)
    else:
        return -1


def queerMember(my_list):

    if len(my_list) > 0:
        avg = average(my_list)
        bigdiff = 0
        index = 0

        #loop through array and get the queer
        for x in range(0, len(my_list)):
           if  bigdiff < abs(my_list[x]) - avg:
               bigdiff = abs(my_list[x]) - avg
               index = x
        return my_list[index]
    else:
        return -1


def smallestelement(my_list):
    index = 0
    for x in range(0, len(my_list)):
        smallE = my_list[x]
        if smallE <= my_list[x]:
            index = x
        return my_list[index]
    else:
        return -1


def main():
    my_list = [-50, 7, 2, 6, 5, 1, 2, 9, 6, 4, 19, 11]
    print("Average of list is: %d " % average(my_list))
    print("Queer element is: %d " % queerMember(my_list))
    print("Smallest element is: %d " % smallestelement(my_list))

 # Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()