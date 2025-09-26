import math

def bisection(f, a, b, k):
    """利用二分法(bisection method)求函数f在区间(a,b)的零点,精确度为k(高中数学必修一 P146)
    >>> f = lambda x: pow(2, x) + 3 * x - 7
    >>> bisection(f, 1, 2, 0.1)
    1.375
    >>> f = lambda x: math.log(x) + 2 * x - 6 # f(x)=ln x+2x-6
    >>> bisection(f, 2, 3, 0.01)
    2.53125
    """

    c = (a + b) / 2
    if f(a) * f(c) < 0:
        if abs(c-a) < k:
            return a
        return bisection(f, a, c, k)
    elif f(c) == 0:
        return c
    else:
        return bisection(f, c, b, k)