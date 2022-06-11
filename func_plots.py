from tkinter import font
from turtle import color
from matplotlib import font_manager
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def make_name(type, args):
    if type == 'logarithmic':
        return f"{args['a']}*log({args['b']}*x + {args['c']}) + {args['d']}"
    if type == 'exponential':
        return f"{args['a']} ** (x*{args['b']} + {args['c']}) + {args['d']}"
    if type == 'sine':
        return f"{args['a']}*sin({args['b']}*x + {args['c']}) + {args['d']}"


def plot_func(f, start, finish, n, **args):
    """
    Plot a function f n elements and calculate integral from start to finish.
    """
    send = tuple(args.values())

    integral = spi.quad(f, start, finish, args=(send))
    y_start = f(start, **args)
    y_finish = f(finish, **args)


    tmp = (finish - start) / 3

    x = np.linspace(start - tmp, finish + tmp, n)
    y = f(x, **args)
    make_title = make_name(f.__name__, args)

    font1 = {'family':'serif','color':'black','size':20} # use for title
    font2 = {'family': 'serif', 'size': 10} # use for labels

    plt.plot(x, y, color='black')
    plt.rc('font', **font2) # sets the default font
    plt.title(f"{make_title}", fontdict=font1)
    plt.suptitle(f"Integral under curve between {start} and {finish}")
    plt.xlabel(f"Integral == {integral[0]}", )
    # plt.fill_between(x,y,min(y),where=x>=start and x<=finish)
    plt.vlines(x=finish,ymin=min(y), ymax=y_finish, color='red', linestyle='--')
    plt.vlines(x=start,ymin=min(y), ymax=y_start, color='red', linestyle='--')
    plt.fill_between(x,y,min(y),where=x>=start,color='lime')
    plt.fill_between(x,y,min(y),where=x>finish,color='white')
    plt.show()


