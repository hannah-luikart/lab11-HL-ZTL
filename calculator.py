"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a,b):
    try:
        return b/a
    except ZeroDivisionError:
        raise

def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise

def exp(a,b):
    return a**b






