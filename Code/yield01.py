def a_then_b(a,b):
    yield from a
    yield from b

def list_partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in list_partitions(n-m, m):
            yield p + ' + ' + str(m)
        yield from list_partitions(n, m-1)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
       return count_partitions(n-m, m) + count_partitions(n, m-1)
