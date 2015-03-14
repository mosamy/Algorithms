#__author__ = 'mohame samyd '
# quick sort

from sys import *

def partition(my_list, start, end):
    length = len(my_list)
    pivot = my_list[start]
    left = start+1
    # Start outside the area to be partitioned

    right = end
    done = False
    while not done:
        while left <= right and my_list[left] <= pivot:
            left = left + 1
        while my_list[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = my_list[left]
            my_list[left] = my_list[right]
            my_list[right] = temp
    # swap start with myList[right]
    temp = my_list[start]
    my_list[start] = my_list[right]
    my_list[right] = temp
    return right


def quick_sort(my_list, start, end):
    if start < end:
        # partition the list
        split = partition(my_list, start, end)
        # sort both halves
        quick_sort(my_list, start, split-1)
        quick_sort(my_list, split+1, end)
    return my_list



def main():
  #print("Hello")
  my_list = [7, 2, 6, 5, 1, 29, 6, 4, 19, 11]
  sorted_list = quick_sort(my_list, 0,  len(my_list)-1)
  print(my_list)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
