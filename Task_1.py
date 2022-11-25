################################################################################
################################ TASK__1 #######################################
################################################################################
"""
Ques 1 - celsius to fahrenheit
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
Ques 3 - table of power of 1, 2, 3 from 0 to 9.
"""
n = 0
while n < 10:
    print(n, "    ", n ** 2, '\t', n ** 3)
    n += 1


def gcd(a, b):
    """
    Question 4 - Greatest Common Divisor
    :param a: first integer
    :param b: second integer
    :return: the second number until the first is zero in a recursive call with the remainder of both num.
    """
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(10, 15))


def fibRe(n):
    """
    Question 5 - Recursive Fibonacci
    :param n: integer number
    :return: the fibonacci of n number
    """
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
Ques 7 - remove a digit from a positive integer.
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


