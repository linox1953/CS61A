def unique_digits(n):
    """这是一个分析n中有几个独特数位的函数"""
    i = 0
    count = 0
    while i <= 9:
        if has_digits(n, i):
            count += 1
        i += 1
    return count

def has_digits(n, k):
    """这是判断n的数位中是否包含k的函数"""
    assert k >= 0 and k < 10, 'Wrong!'

    while n:
        if n % 10 == k:
            return True
        n //= 10
    return False