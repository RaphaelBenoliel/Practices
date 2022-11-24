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


print(randNumber())
