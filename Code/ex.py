def count(s, value):
    """Count the number of times that value occurs in sequence S
    """
    total, index = 0, 0
    while index < len(s):
        element = s[index]
        if element == value:
            total += 1
        index += 1
    return total