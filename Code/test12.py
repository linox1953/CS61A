def print_x(n: int):
    print((6-n) * " " + "*" * 6)
    if n == 0:
        return
    print_x(n-1)
    print((6-n) * " " + "*" * 6)

print_x(6)