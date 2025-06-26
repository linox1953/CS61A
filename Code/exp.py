def exp(b, n): # linear time, common
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def exp_fast(b, n): # logarithmic time, scales very large input
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

def overlap(a, b): # quadratic time, slow but common
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count

def fast_overlap(a, b): # linear time, perhaps
    i, j, count = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif a[i] < b[i]:
            i += 1
        else:
            j += 1
    return count

def fib(n): # exponential time, very slow
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def square(x):
    return x * x
