import math, timeit, sys
#from pkg import string
import pkg.spam


[print(x) for x in sys.path]


def adder(*pargs):
    sum = pargs[0]
    for i in pargs[1:]:
        sum += i
    return sum

print(adder('grecha', 'anna'))
print(adder(2, 6, 1))
print(adder(2.56, 1.21))
print(adder(['a', 'b'], [3, 7]))

def adder2(**kargs):
    keys = list(kargs.keys())
    sum = kargs[keys[0]]

    for x in keys[1:]:
        sum += kargs[x]

    return sum

print(adder2(good=2, ugly=4, gr=10))

def copyDict(d):
    return d.copy()

d = {'a':1, 'b':2}

d1 = copyDict(d)

d2 = {'r':8, 'h':0}

d['a'] = 5

print(d, d1)

def addDict(d1, d2):
    #if type(d1) is dict:
    if isinstance(d1, dict):
        d1.update(d2)
        return d1
    #elif type(d1) is list:
    elif isinstance(d1, list):
        return d1 + d2



l1 = list('grecha')
l2 = list('anna')

#print(type(d))

print(addDict(d, d2))
print(addDict(l1, l2))

def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)
def f3(a, **b): print(a, b)
def f4(a, *b, **c): print(a, b, c)
def f5(a, b=2, c=3): print(a, b, c)
def f6(a, b=2, *c): print(a, b, c)

def simple(y):
    y = abs(y)
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'имеет делитель', x)
            break
        x -= 1
    else:
        print(y, 'это простое число')


l = [2, 4, 9, 16, 25]
"""
import math

res = []
for i in l: res.append(math.sqrt(i)); print(res)

print("\n")
import timeit

print('for', min(timeit.repeat(
        stmt="for i in l: res.append(math.sqrt(i))",
        setup="import math\nl = [2, 4, 9, 16, 25]\nres = []",
        number=10000,
        repeat=5
        )))


print('map', min(timeit.repeat(
        stmt="list(map(math.sqrt, l))",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('list', min(timeit.repeat(
        stmt="[math.sqrt(i) for i in l]",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('gen', min(timeit.repeat(
        stmt="list(math.sqrt(i) for i in l)",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print("\n")

print('for', min(timeit.repeat(
        stmt="for i in l: res.append(i ** .5)",
        setup="import math\nl = [2, 4, 9, 16, 25]\nres = []",
        number=10000,
        repeat=5
        )))


print('map', min(timeit.repeat(
        stmt="list(map(lambda i: i ** .5, l))",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('list', min(timeit.repeat(
        stmt="[i ** .5 for i in l]",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('gen', min(timeit.repeat(
        stmt="list(i ** .5 for i in l)",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))


print("\n")

print('for', min(timeit.repeat(
        stmt="for i in l: res.append(pow(i, .5))",
        setup="import math\nl = [2, 4, 9, 16, 25]\nres = []",
        number=10000,
        repeat=5
        )))


print('map', min(timeit.repeat(
        #stmt="list(map(lambda i: pow(i, .5), l))",
        stmt="list(map(pow, l, [.5 for _ in range(len(l))]))",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('list', min(timeit.repeat(
        stmt="[pow(i, .5) for i in l]",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))

print('gen', min(timeit.repeat(
        stmt="list(pow(i, .5) for i in l)",
        setup="import math\nl = [2, 4, 9, 16, 25]",
        number=10000,
        repeat=5
        )))
"""


def countdown(x):
    if not x:
        print('stop')
    else:
        print(x, end=' ')
        x -= 1
        countdown(x)

countdown(5)


def gen1(x):
    for i in range(x, -1, -1):
        if not i:
            yield('stop')
            break
        yield i

#a = ' '.join(gen1(5))

print(' '.join([str(x) for x in gen1(5)]))

#print(next(a))
#print(next(a))
#print(next(a))


def fact1(n):
    if n >= 1: return n * fact1(n-1)
    else: return 1

print(fact1(6))

from functools import reduce

def fact2(n):
    return reduce(lambda a, b: a * b, range(1, n+1))

print(fact2(6))

def fact3(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(fact3(6))

def fact4(n):
    return math.factorial(n)

print(fact4(6))


print('fact1', min(timeit.repeat(
        stmt="fact1(6)",
        setup="def fact1(n):\n\tif n >= 1:\n\t\treturn n * fact1(n-1)\n\telse:\n\t\treturn 1",
        number=10000,
        repeat=5
        )))

print('fact2', min(timeit.repeat(
        stmt="fact2(6)",
        setup="from functools import reduce\ndef fact2(n):\n\treturn reduce(lambda a, b: a * b, range(1, n+1))",
        number=10000,
        repeat=5
        )))

print('fact3', min(timeit.repeat(
        stmt="fact3(6)",
        setup="def fact3(n):\n\tres = 1\n\tfor i in range(1, n+1):\n\t\tres *= i\n\treturn res",
        number=10000,
        repeat=5
        )))

print('fact4', min(timeit.repeat(
        stmt="fact4(6)",
        setup="import math\ndef fact4(n):\n\treturn math.factorial(n)",
        number=10000,
        repeat=5
        )))

print('\n')

print(min(timeit.repeat(stmt=lambda: fact1(6), number=10000, repeat=5)))
print(min(timeit.repeat(stmt=lambda: fact2(6), number=10000, repeat=5)))
print(min(timeit.repeat(stmt=lambda: reduce(lambda a, b: a * b, range(1, 6+1)), number=10000, repeat=5)))
print(min(timeit.repeat(stmt=lambda: fact3(6), number=10000, repeat=5)))
print(min(timeit.repeat(stmt=lambda: fact4(6), number=10000, repeat=5)))
print(min(timeit.repeat(stmt=lambda: math.factorial(6), number=10000, repeat=5)))