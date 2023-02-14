# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
import math as m


def binom(a, b):
    res = m.factorial(a) / (m.factorial(b) * (m.factorial(a - b)))
    return res


a = list(map(int, input().split()))
d = dict()
res = 0
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] > 1:
        res += binom(d[i], 2)
print(int(res))