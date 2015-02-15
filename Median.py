def median(lst):
    lst = sorted(lst)
    retmedian = 0
    index = 0
    if len(lst) == 1:
        retmedian = 1
    elif len(lst) % 2 == 0:
        #even number
        retmedian = (lst[len(lst) / 2 - 1] + lst[len(lst) / 2]) / 2.0
    else:
        retmedian = lst[len(lst) / 2]

    return retmedian


print median([1,2,3,4])