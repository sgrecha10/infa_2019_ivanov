"""
tmp = open

def newopen(*args, **kargs):
    print('Hi! Newopen working!')
    return tmp(*args, **kargs)

open = newopen

f = open('out.txt')
for s in f: print(s, end='')

import sys

# f3 = lambda x: [sys.stdout.write(n) for n in x]
# f3(('123\n', '456\n', '6789\n'))

def f2(x):
    [sys.stdout.write(n) for n in x]

f2(('123\n', '456\n', '6789\n'))
"""


def gen():
    yield "yield"
    return "return Mess"

g = gen()

try:
    print(next(g))
    print(next(g))
except StopIteration as s:
    print(s)