def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    def find_ways(k, j):
        if k > m:
            return 0
        elif j > n:
            return 0
        elif k == m and j == n:
            return 1
        else:
            return find_ways(k+1, j) + find_ways(k, j+1)
    return find_ways(1, 1)