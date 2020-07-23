
def f(sum):
    l.append(sum)
    print(l)
    # print(sum)

l=[]
f(10)
f(10)
# f(10, l)
# f(10, l)
f(10)
f(10)
# print(l)

def foo(x):
    def boo(t):
        s = x + t
        print(s)
    return boo

a = foo(5)
b = foo(50)
a(3)
b(2)
print(id(a))
print(id(b))


import time


def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            ex_time = time.time() - start_time
            print('Execution time:', ex_time)
    return inner


def measure_time2(func):
    start_time = time.time()
    try:
        return func
    finally:
        ex_time = time.time() - start_time
        print('Execution time:', ex_time)



@measure_time
def slow_func():
    print("Начали")
    time.sleep(1)
    print("Кончили")


# slow_func = measure_time(slow_func)

slow_func()

input("Press Enter")
