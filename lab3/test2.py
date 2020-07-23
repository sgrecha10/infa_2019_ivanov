"""
>>> f1()
at index 56

"""


L = []
for n in range(7):
    L.append(2**n)

L = list(map(lambda x: 2**x, range(7)))

print(L)

X = 5
i = 0

Xs = 2 ** X
" тут описалово после даты"
while i<len(L):
    if Xs == L[i]:
        print('at index', i)
        break
    else:
        i = i + 1
else:
    print(X, 'not found')


for i, n in enumerate(L):
    if Xs == L[i]:
        print('at index', i)
        break
else:
    print(X, 'not found')


for n in L:
    if Xs == n:
        print('at index', L.index(n))
        break
else:
        print(X, 'not found')
def f1():
    "Описалого функции f1"
    if Xs in L:
            print('at index', L.index(Xs))
    else:
            print(X, 'not found')

f1()


import sys
print('test2' in sys.modules)



import doctest
doctest.testmod()

