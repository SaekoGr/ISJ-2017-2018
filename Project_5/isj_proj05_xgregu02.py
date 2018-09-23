#!/usr/bin/env python3

import collections
from math import factorial

class Polynomial:
    """ class Polynomial receives arguments as list or tupple """
    def __init__(self, *args, **kwargs):
        """ converts all the input data into list """
        # temporary list
        indexes = []
        # arguments is a tupple, so args[0] is taken and converted into list
        if args and isinstance(args[0], list):
            args = args[0]
        # argument is list and there are no kwargs
        elif isinstance(args, tuple) and kwargs == {}:
            args = list(args)
        # argument is directory; it is converted into list
        else:
            args = [kwargs.get(x, 0) for x in ['x' + str(i) for i in range(len(kwargs) + 1)]]
        # list is reversed and saved
        args.reverse()
        self.args = args


    def __str__(self):
        """ formats the output into the desired format """
        # help list variable
        polynom = []
        first = -1

        # find the first non zero arguments
        for i in range (0, len(self.args)):
            if self.args[i] != 0:
                first = i
                break

        # goes throught all the arguments and formats them
        for i in range(0, len(self.args)):
            # zero values are skipped
            if self.args[i] == 0:
                continue
            # exponent variable
            exponent = len(self.args)-i-1

            # check the sign
            # '+' cannot be shown before the first argument and also at the end
            if first !=i and i !=0 and int(self.args[i]) > 0:
                sign = "+"
                polynom.append(sign)
            elif int(self.args[i]) < 0:
                sign = "-"
                polynom.append(sign)

            # add the exponent value formated accordingly
            if exponent == 1:
                if abs(self.args[i]) == 1:
                    item = "x"
                else:
                    item = str(abs(self.args[i])) + "x"
            elif exponent == 0:
                item = str(abs(self.args[i]))
            else:
                if abs(self.args[i]) == 1:
                    item = "x^" + str(exponent)
                else:
                    item = str(abs(self.args[i])) + "x^" + str(exponent)
            # final value is appended
            polynom.append(item)

        # if the list comes out blank, the result is 0
        if polynom == []:
            return str(0)
        # else return the list joined by whitespaces
        else:
            return " ".join(polynom)

    def __eq__(self, other):
        """ checks whether the 2 lists are equal or not """
        for i in range(1, len(self.args)):
            return self.args[i] == other.args[i]

    def __add__(self, other):
        """ adds up 2 lists """
        bigger = self.args
        smaller = other.args
        result = []

        # make sure the bigger one is bigger
        if len(bigger) < len(smaller):
            bigger, smaller = biggger, smaller

        # add the numbers that are would be added only with zero and delete them
        # so the 2 lists have same lenght
        while len(bigger) > len(smaller):
            result.append(bigger[0])
            bigger.remove(bigger[0])

        # add the elements at the same place and append it to item
        for i in range (0, len(bigger)):
            item = bigger[i] + smaller[i]
            result.append(item)

        # reverse the result
        result.reverse()

        return str(Polynomial(result))

    def at_value(self, x, y=None):
        """ calculates the value of polynom for given number """

        # calculate self.at_value(y) and subtract self.at_value(x)
        if y is not None:
            return self.at_value(y) - self.at_value(x)

        # help variables
        result = 0
        k = 0
        # add up every argument times x to the i
        for i in range(len(self.args)-1, -1, -1):
            result += self.args[k] * (x ** i)
            k += 1

        # result is returned
        return result

    def derivative(self):
        """ calculates the derivative of the polynom """
        # help variables
        result = []
        k = 0

        # calculate the derivative of each element and append it to the list result
        for i in range(len(self.args)-1, -1, -1):
            item = self.args[k] * i
            result.append(item)
            k += 1

        # the last element if derivation is deleted
        del result[-1]

        # reverse the list and return it
        result.reverse()
        return Polynomial(result)

    def __pow__(self, order):
        """ calculates the power by binomical theorem """
        # search for the furst non-zero element
        first = -1
        for i in self.args:
            if i != 0:
                first = i
                break

        # deletes arguments that is zero
        for i in range(0, first):
            del self.args[i]

        # creates helps variables and calculates the numerator
        result = []
        self.args.reverse()
        x = self.args[0]
        y = self.args[1]
        top = factorial(order)

        # calculates value by binomical theorem and appends it to the list
        for i in range(0, order+1):
            binom = int(top/(factorial(i)*factorial(order-i)))
            item = binom*(x**(order-i))*(y**(i))
            result.append(item)

        return Polynomial(result)

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
