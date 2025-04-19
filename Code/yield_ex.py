def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def for_prefixes(s):
    result = []
    if s:
        for p in for_prefixes(s[:-1]):
            result.append(p)
        result.append(s)
    return result

def list_partitions(m, n):
    if m > 0 and n > 0:
        if m == n:
            yield str(n)
        for x in list_partitions(m-n, n):
            yield x + ' + ' + str(n)
        yield from list_partitions(m, n-1)

def count_partitions(m, n):
    if m == 0:
        return 1
    elif m < 0 or n == 0:
        return 0
    else:
        return count_partitions(m-n, n) + count_partitions(m, n-1)
        
print(list(prefixes('dogs')))
print(for_prefixes('dogs'))
for p in list_partitions(6, 4): print(p)
print(count_partitions(6, 4))