#!/usr/bin/env python
# coding: utf-8

import math


# ### Произведём процедуру отделения корней:
# 
# Будем разбивать отрезок $[A, B]$ на дизъюнктные отрезки длины $\frac{B - A}{N}, N \in \mathbb{N}$
# 
# Если функция меняет знак на концах отрезка, то по теореме Больцано-Коши она принимает нулевое значение.
# 
# Критерием останова будет факт того, что количество корней не увеличивается в течение $T$ иттераций.
# 
# Для функций, у которых невозможно отделить нули (например $\sin{\frac{1}{x}}$), предусмотрено ограничение в **MAXN** иттераций.

# In[3]:

def make_root_separation(A, B, func):
    MAXN = 100
    t = 10
    target_times = 0
    zero_times = 0
    section_list = []
    flag = True
    N = 1
    while target_times < t:
        if N > MAXN:
            flag = False
            print("Не удалось отделить корни")
            break
        instant_zero_times = 0
        instant_section_list = []
        for i in range(N):
            a = A + i * (B - A) / N
            b = A + (i + 1) * (B - A) / N
            if func(a) * func(b) <= 0:  # non strict comparing
                instant_zero_times += 1
                instant_section_list.append([a, b])
        if instant_zero_times == zero_times:
            target_times += 1
        else:
            target_times = 0
        zero_times = instant_zero_times
        section_list = instant_section_list
        N += 1
    return zero_times, section_list


# ### Уточним корни на всех найденных отрезках перемены знака
# 
# #### Метод бисекции

# In[4]:

def get_roots(a, b, func, epsilon):
    zero_times, section_list = make_root_separation(a, b, func)
    answer_list = []
    print(zero_times)
    for i in range(zero_times):
        a, b = section_list[i]
        steps = 0
        while (b - a) >= 2 * epsilon:
            c = (b + a) / 2
            if func(a) * func(c) <= 0:  # non strict comparing
                b = c
            elif func(c) * func(b):
                a = c
            steps += 1

        steps += 1
        ans = (a + b) / 2

        answer_list.append(ans)

    return answer_list
