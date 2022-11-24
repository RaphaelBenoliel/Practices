################################################################################
################################ Task__3 #######################################
################################################################################
def collect(n):
    """
    Ques 1 -
    :param n:
    :return:
    """
    if n is None:
        return ()
    x, y = n
    return (x,) + collect(y)


print(collect((1, (2, None))))


def integral(a, b, f):
    sum = (b - a) / 1000
    for i in range(0, 1000):
        sum += f * (a + (i * (b - a) / 1000))
    return sum


print(integral(-1, 100, 3))


def fibo_build(a, b):
    def fibo(n):
        if n == 0:
            return a
        if n == 1:
            return b
        return fibo(n - 1) + fibo(n - 2)

    return fibo


z = fibo_build(10, 20)
print(z(6))


def fun(x):
    return x + 1


def smooth(f):
    def g(n):
        return (f(n - 1) + f(n) + f(n - 1)) / 3

    return g


a = smooth(fun)
print(a(4))
"""
from turtle import *

color('red', 'yellow')
begin_fill()
for i in range(36):
    forward(200)
    left(170)
end_fill()
done()
"""