# refactor calculator.py

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
        
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        
        return a / b

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def log(a):
    return math.log(a)

def exp(a):
    return math.exp(a)

def sqrt(a):
    return math.sqrt(a)

def factorial(a):
    return math.factorial(a)

# refactor unittestsforcalculator.py

