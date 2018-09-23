#!/usr/bin/env python3

def can_be_a_set_member_or_frozenset(item):
    """ checks whether item can be an element of set """
    # checks whether it is int or tupple, if yes, it return the item as it is
    if isinstance(item, int) or isinstance(item, tuple):
        return item
    # if it isn't int or tuple, return it as a frozenset
    else:
        return frozenset(item)

def all_subsets(lst):
    """ creates all subsets only with build-in functions """
    # creates 2 temporary lists
    perm_list = []
    item = []
    # variable for the second for cycle
    i = 0

    # for every letter in lst, iterate throught it
    for letter in lst:
        # append single letter
        perm_list.append([letter])
        # iterate for x in range(0, i)
        # variable i is the number of all previous subsets of original set
        for x in range(0, i):
            # deep copy of perm_list[x]
            item = perm_list[x][:]
            # add it up to a single list in variable item
            item += letter
            # hard copy of item to perm_list
            perm_list += [item][:]
        # variable i is always its sum plus one
        i = i + i + 1

    # prepare final_list
    final_list = []
    # the first subset is empty
    final_list.append([])
    # the perm_list is added
    final_list += perm_list[:]
    # returns final_list
    return final_list

def all_subsets_excl_empty(*args, **kwargs):
    """ creates all subsets only with build-in functions
        with the choice of inclusion/exclusion of the first empty subset"""
    # tupple of arguments is converted into list
    lst = list(args)
    # empty final_list is created
    final_list = []

    # if kwargs is empty, pass
    if kwargs == {}:
        pass
    # if kwargs['exclude_empty'] is True, pass
    elif kwargs['exclude_empty'] == True:
        pass
    # if kwargs['exclude_empty'] is False, the first empty list is appended
    elif kwargs['exclude_empty'] == False:
        final_list.append([])

    # 2 empty lists are created
    perm_list = []
    item = []
    i = 0

    # for every letter in lst, iterate throught it
    # number of iterations equals to len(lst)
    for letter in lst:
        # append single letter
        perm_list.append([letter])
        # variable i is the number of all previous subsets of original set
        for x in range(0, i):
            # deep copy of perm_list[x]
            item = perm_list[x][:]
            # add it up to a single list in variable item
            item += letter
            # hard copy of item to perm_list
            perm_list += [item][:]
        # variable i is always its sum + 1
        i = i + i + 1

    # perm_list is added to final_list
    final_list += perm_list[:]
    # return final_list
    return final_list
