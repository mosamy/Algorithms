
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


def main():
    my_list = [7, 2, 6, 5, 1, 29, 6, 4, 19, 11]
    print("Average of list is: %d " % average(my_list))

 # Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
