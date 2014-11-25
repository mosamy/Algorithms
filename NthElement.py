__author__ = 'mohamed'
#nth element from the bottom

def nthelementfrombottom (n, my_list):
    if len(my_list) > n:

        return my_list[len(my_list)-n]
    else:
        return -1


def main():
    my_list = [7, 2, 6, 5, 1, 29, 6, 4, 19, 11]
    print(nthelementfrombottom(2, my_list))

 # Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()