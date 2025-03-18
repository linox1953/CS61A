def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if not s:
        return 1
    def get_mul(s, i):
        if i >= len(s):
            return 1
        else:
            return max(s[i] * get_mul(s, i+2), get_mul(s, i+1))
    return get_mul(s, 0)