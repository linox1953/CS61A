def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value
    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    # method 1
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
    # method 2
    f = lambda i: abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    """
    # method 1
    return max(s[i] + s[i+1] for i in range(len(s) - 1))
    # method 2
    return max([a + b for a, b in zip(s[:-1], s[1:])])

def digit_dict(s):
    """Map each digit d to the lists of elements in s that
    end with d
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [99]}
    """
    last_digit = [x % 10 for x in s]
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digit}
    
def all_have_an_equal(s):
    """Does every element equal some other elements
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 2, 3, 4])
    True
    """
    return all(s[i] in s[:i] + s[i+1:] for i in range(len(s)))