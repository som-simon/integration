import numpy as np

def integrate_with_n(f, a, b, n):
    """
    Integrate a function f from a to b using n rectangles.
    """
    h = (b - a) / n
    x = np.arange(a, b, h)
    y = f(x)
    return h * np.sum(y)


def integrate_with_n_trapz(f, a, b, n):
    """
    Integrate a function f from a to b using n trapezoids.
    """
    h = (b - a) / n
    x = np.arange(a, b, h)
    y = f(x)
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))