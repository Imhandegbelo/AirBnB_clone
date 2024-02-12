#!/usr/bin/python3

def add(a, b):
    """adds two numbers"""

    if type(a) != int or type(a) != float:
        raise TypeError("Expected a to be a number")
    if type(b) != int or type(b) != float:
        raise TypeError("Expected a to be a number")
    return a + b
