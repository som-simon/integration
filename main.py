import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from func_plots import make_name, plot_func
from calculation_funcs import *
import custom_algorithms as ca


def exec(f, start, finish, n, **args):
    """
    Plot a function f n elements and calculate integral from start to finish.
    """
    send = tuple(args.values())
    integral = spi.quad(f, start, finish, args=(send))

    print(f'Integrate {make_name(f.__name__, args)} from {start} to {finish} using scipy.integrate.quad:')
    print('    {}'.format(integral[0]))
    plot_func(f, start, finish, n, **args)

if __name__ == '__main__':
    matplotlib.use('TkAgg')
    
    start = 0
    finish = np.pi
    n = 1000

    q,w,e,r = 2.3,3.7,9.1,5.0

    exec(exponential, start, finish, n, a=q,b=w,c=e,d=r)


