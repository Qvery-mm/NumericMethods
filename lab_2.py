#!/usr/bin/env python
# coding: utf-8



def z_k(k, z, n, values):
    product = 1
    for p in range(n + 1):
        if p != k:
            product *= (z - values[p][1])
    return product


def lagrange(q, n, values, x):
    ans = 0
    for t in range(n + 1):
        ans += values[t][2] * z_k(t, x, n, values) / z_k(t, values[t][1], n, values)
    return ans


# In[3]:

def interpolate_and_get_result(values, n, x):

    if x == values[0][1]:
        return values[0][2]

    else:
        return lagrange(x, n, values, x)

