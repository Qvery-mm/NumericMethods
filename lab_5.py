import math
import numpy as np
from sympy import Symbol, integrate, lambdify, solve, re

x = Symbol('x')


def definite_integral(func, a, b):
    indefinite_integral = lambdify(x, integrate(func, x))
    return indefinite_integral(b) - indefinite_integral(a)


def formula(f, table, A, B):
    w = 1
    X = list(table['x'])
    Y = list(table['Tn(x)'])
    omega = (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3]) * (x - X[4])
    d_omega = lambda x: (5 * x ** 4 -
                         4 * x ** 3 * (sum(X)) +
                         3 * x ** 2 * (X[0] * X[1] + X[0] * X[2] + X[0] * X[3] + X[0] * X[4] + X[1] * X[2] +
                                       X[1] * X[3] + X[1] * X[4] + X[2] * X[3] + X[2] * X[4] + X[3] * X[4]) -
                         2 * x ** 1 * (X[0] * X[1] * X[2] + X[0] * X[1] * X[3] + X[0] * X[1] * X[4] +
                                       X[0] * X[2] * X[3] + X[0] * X[2] * X[4] + X[0] * X[3] * X[4] +
                                       X[1] * X[2] * X[3] + X[1] * X[2] * X[4] + X[1] * X[3] * X[4] +
                                       X[2] * X[3] * X[4]) +
                         1 * x ** 0 * (X[0] * X[1] * X[2] * X[3] + X[0] * X[1] * X[2] * X[4] + X[0] * X[1] * X[4] * X[3] +
                                       X[0] * X[4] * X[2] * X[3] + X[4] * X[1] * X[2] * X[3])
                         )

    I_Gauss_type = sum(definite_integral(omega / (x - X[i]) / d_omega(X[i]), A, B) * f(X[i], Y[i]) for i in range(5))
    return Y[4] + I_Gauss_type
