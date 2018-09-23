#!/usr/bin/env python3
import collections
import itertools


def first_nonrepeating(string):
    """ Goes throught a string and find the first nonrepeating elemnt """

    # checks whether string is space or tabulator
    if string == ' ' or string == '\t':
        return None

    # if input is not in the correct format
    elif isinstance(string, int) or isinstance(string, dict):
        return

    elif isinstance(string, set):
        return

    # create new empty list
    tmp_list = []
    # goes through string and appends all unique characters
    for i in string:
        if i in tmp_list:
            pass
        else:
            tmp_list.append(i)
    # iterate through the list and find the first
    #character that exists only 1 time string
    for i in tmp_list:
        count = string.count(i)
        if count == 1:
            return i

    return None


def combine4(numbers, result):
    """ Calculates all possible combinations and find the correct one """

    # returns if insufficient number of arguments
    if len(numbers) != 4:
        return

    # convert numbers into list
    numbers = [str(float(n)) for n in sorted(numbers)]
    # creates temporary lists
    final = []
    tmp_final = []
    tmp = []

    # iterate throught all number combinations
    # and create list with all possible options
    for n in itertools.permutations(numbers, 4):
        # iterate through all sign combinations
        for operations in itertools.product("+-*/", repeat=len(n) - 1):
            # convert to number_perms
            number_perms = list(n)
            # inset operations between numbers
            for j, operation in enumerate(operations):
                number_perms.insert(j * 2 + 1, operation)
            # iterate through brackets
            for left_bracket in range(0, len(n) -1):
                for right_bracket in range(left_bracket + 2, len(n) + 1):
                    # expression is prepared
                    expression = list(number_perms)
                    # brackets are added
                    expression.insert(2 * right_bracket - 1, ")")
                    expression.insert(2 * left_bracket, "(")
                    # list is appended
                    tmp.append(expression)


    # find only the suitable combinations
    for k in tmp:
        result_of_calculation = "".join(k)
        try:
            # check whether evaluated values equals result
            if eval(result_of_calculation) == result:
                # append it to the final list
                tmp_final.append(k)
            # skip zero divsion
        except ZeroDivisionError:
            continue

    # iterate through final list
    for n in tmp_final:
        # remove brackets if they are on the first and last place
        if n[0] == "(" and n[8] == ")":
            n = n[1:8]
        # remove all the floats
        for position, i in enumerate(n):
            if ".0" in i:
                i = i.replace(".0", "")
                n[position] = i
        # join it and append
        values = "".join(v for v in n)
        final.append(values)

    # final list is converted to set and immediately back to list
    # in order to get rid of duplicates
    final = list(set(final))
    return final
