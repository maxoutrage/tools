#!/usr/bin/python3
#
# Tools package (Fuel 0.01\
#
import sys
#
"""
Slurp returns the contens of a file as a list
"""


def slurp(filename):
    try:
        my_file = open(filename, "r")
    except OSError as e:
        print("OS Error: {0}".format(e))
    else:
        content = my_file.read()
        content_list = content.splitlines()
        my_file.close()
        return content_list
#


def placeholder():
    return("EOF")


def get_ints():
    ints = list(map(int, input().split()))
    return(ints)


def get_strs():
    strs = list(map(str, input().split()))
    return(strs)
