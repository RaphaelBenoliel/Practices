################################################################################
################################ TASK__1 #######################################
################################################################################
'''
"""
Ques 1 - celsius to far
"""
degree = float(input('Enter Celcius: '))
far = (9 / 5 * degree) + 32
print(far)

"""
Ques 2 - n! factorial
"""
f = 1
n = 0
for i in range(60):
    print(n, '! =', f)
    n += 1
    f *= n


"""
Ques 3 -
"""
n = 0
while n < 10:
    print(n, "    ", n ** 2, '\t', n ** 3)
    n += 1


"""
Ques 4 -
"""
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(10, 15))

"""
Ques 5 - Fibonacci
"""
def fibRe(n):
    if n <= 1:
        return n
    return fibRe(n - 1) + fibRe(n - 2)


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fibo(9))

"""
Ques 6 - Prefect number
"""
def prefect_number(n):
    i = 1
    sum = 0
    for i in range(i, n):
        if n % i == 0:
            sum += i
    if n == sum:
        return True
    return False


if prefect_number(20):
    print('Is prefect number')
else:
    print('hara AleHa!')
for i in range(10001):
    if prefect_number(i):
        print(i)


"""
Ques 7 -
"""
def appear(bigNum, a):
    s, f, mul, newNum = 1, 10, 1, 0
    for i in range(5):
        n = bigNum % f // s
        s *= 10
        f *= 10
        if a != n:
            newNum += n * mul
            mul *= 10
    return newNum


print(appear(53832, 3))

################################################################################
################################ Task__2 #######################################
################################################################################
import random


def Binary(n):
    for i in range(n):
        binary = random.randint(0, 255)
        print(format(binary, '08b'))


Binary(5)

"""
ques 2 -
"""
def foo(n):
    return set(str(n).replace('.', ''))


y = 5.9998765
print(foo(y))

"""
Ques 3 -
"""
def sqt(n):
    for i in range(n + 1):
        if i*i == n:
            return i


print(sqt(16))

"""
Ques 4 - entering positive numbers till a negative numbers  return list of all pos numbers.
"""
def positiveNum():
    l = []
    while True:
        n = int(input('Enter a positive number: '))
        if n < 0:
            return l
        l.append(n)


print(positiveNum())

"""
Ques 5 - find minimum sum and maximum in a list
"""
def MinMaxSum():
    l = []
    minMaxSum = []
    size = int(input('Enter size of list: '))
    print('Enter numbers to list: ')
    for i in range(size):
        n = int(input())
        l.append(n)
    minMaxSum.append('MIN: ' + str(min(l)))
    minMaxSum.append('SUM: ' + str(sum(l)))
    minMaxSum.append('MAX: ' + str(max(l)))
    return minMaxSum


print(MinMaxSum())

"""
Ques 6 - concatenation of two list
"""
def Concatenation(a, b):
    c = []
    k = 0
    for i in a:
        for j in range(b[k]):
                c.append(i)
        k += 1
    return c


print(Concatenation([6, 7, 8], [2, 1, 3]))

"""
Ques 7 - 
"""
def dictionary(n):
    s = set(str(n))
    print(n, s)

    d = {}
    r = 0
    for i in s:
        d[r] = i
        r += 1
    print(d)


dictionary(random.randint(2, 101))

"""
Ques 8 - list of random numbers
"""
def randNumber():
    l = []
    for i in range(1000):
      l.append(random.randint(1, 10))
    return l


#print(randNumber())

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
    return (x, ) + collect(y)


#print(collect((1, (2, None))))


def integral(a, b, f):
    sum = (b - a) / 1000
    for i in range(0, 1000):
        sum += f * (a + (i * (b-a)/1000))
    return sum


#print(integral(-1, 100, 3))


def fibo_build(a, b):
    def fibo(n):
        if n == 0:
            return a
        if n == 1:
            return b
        return fibo(n - 1) + fibo(n - 2)
    return fibo


z = fibo_build(10, 20)
#print(x(6))

'''
def smooth(f):
    def g(n):
        return (f(n-1)+f(n)+f(n-1)) / 3
    return g


a = smooth(9)
print(a)
'''
from turtle import *
color('red', 'yellow')
begin_fill()
for i in range(36):
    forward(200)
    left(170)
end_fill()
done()
'''
################################################################################
################################ Task__4 #######################################
################################################################################