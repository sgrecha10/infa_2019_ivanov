# author: Grechnev Sergey
"""Module for test

"""
def factorial(n):
    x = 1
    for i in range(1, n+1):
        x += i
    return x

if __name__=='__main__':
    import doctest as dk
    dk.testmod()