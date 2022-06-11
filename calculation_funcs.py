import numpy as np


# def rename(newname):
#     def decorator(f):
#         f.__name__ = newname
#         return f
#     return decorator

def f(x):
    return np.sin(x)


def sine(x, a=1.0,b=1.0,c=0.0,d=0.0):
    return a * np.sin(b*x+c) + d

def exponential(x, a=1.0, b=1.0, c=0.0, d=0.0):
    return a ** (b * x +c) + d

def logarithmic(x, a=1.0, b=1.0, c=0.0, d=0.0):
    return a * np.log(b * x +c) + d