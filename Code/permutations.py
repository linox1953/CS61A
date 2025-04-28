def permutations(s):
    """Yield permutations of list s
    
    >>> list(permutation([1, 2 ,3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if len(s) == 0:
        yield []
    for i in range(len(s)):
        start = s[i]
        rest = [s[j] for j in range(len(s)) if j != i]
        for rest_permutation in permutations(rest):
            yield [start] + rest_permutation