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
    except:
        return ("ValueError")

def hypotenuse(a, b):
    return math.hypoty(a, bg)

def add(a, b): 
    return a + b

def subtract(a,b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a,b):
    try:
        return b/a
    except:
        return "ZeroDivisionError"

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        return "ValueError"

def exponent(a,b):
    return a**b



