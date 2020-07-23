print("приве ", __name__)
print('Я', 'работаю')

print('im', 'work', 2+7)


def f(x):
    x = str(x)[::-1]
    s, i = 0, 1
    for r in x:
        s += int(r)*i
        i *= 2
    print(s)


f