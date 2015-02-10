__author__ = 'mohamed'


def remove_duplicates(lst):
    newlst =[]

    for itm in lst:
        if itm not in newlst:
            newlst.append(itm)
    return newlst
                