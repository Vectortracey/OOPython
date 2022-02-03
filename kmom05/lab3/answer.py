#!/usr/bin/env python3

"""
4e767e722353660e6f0ec190111bf67b
oopython
lab3
v2
miek19
2021-08-18 08:29:27
v4.0.0 (2019-03-05)

Generated 2021-08-18 10:29:27 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `12` up to `33`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def calc_recursive_sum(start=12, end=33):
    """
    calculates the sum of numbers between 12 to 33 and returns it
    """
    if start < end:
        return start + end + calc_recursive_sum(start + 1, end - 1)
    if start > end:
        return 0
    return start


ANSWER = calc_recursive_sum()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that searches for the maximum
# element of a list and returns that number.
# Find the maximum value in the list `[1, 2, 3, 4, 13, 6, 7, 8, 9]`.
#
# Answer with the maximumx value.
#
# Write your code below and put the answer into the variable ANSWER.
#



list_lab = [1, 2, 3, 4, 13, 6, 7, 8, 9]
def recursive_max(mylist):
    "lab3"
    if len(mylist) == 1:
        return mylist[0]
    if mylist[0] > recursive_max(mylist[1:]):
        return mylist[0]
    return recursive_max(mylist[1:])

ANSWER = recursive_max(list_lab)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `4` in the list `[1, 2, 3, 4, 13, 6, 7, 8, 9]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_find(mylist, number=4, index=0):
    """
    searches list for number and returns the index of it
    """
    if mylist[index] == number:
        return index
    if index < len(mylist) - 1:
        return recursive_find(mylist, number, index + 1)
    return -1

ANSWER = recursive_find(list_lab)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `20` in
# the list `[1, 2, 3, 4, 13, 6, 7, 8, 9]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#





ANSWER = recursive_find(list_lab , 20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `11` to the
# power of `3`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_pow(value, n):
    """
    calculates 11 to the power of 3 and returns it
    """
    if n == 1:
        return value
    return value * recursive_pow(value, n - 1)

ANSWER = recursive_pow(11, 3)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Switchy mc switch" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

mystring = "Switchy mc switch"

def recursive_reverse_str(string):
    """
    turns a string backwards and returns it
    """
    if len(string) == 1:
        return string
    return string[-1] + recursive_reverse_str(string[0:-1])

res = recursive_reverse_str(mystring)

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a recursive function in the code below that calculates the "lowest
# common multiple" between two numbers.
# It should return the smallest positive integer that is divisible by both
# "2" and "3".
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_lowest_common_multiple(nr=1, div1=2, div2=3):
    """
    returns the smallest positive integer divisible by both 2 and 3
    """
    if nr % div1 == 0 and nr % div2 == 0:
        return nr
    return recursive_lowest_common_multiple(nr + 1)

ANSWER = recursive_lowest_common_multiple(3)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)


dbwebb.exit_with_summary()
