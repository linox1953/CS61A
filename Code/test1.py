def print_x(n):
    def helper(k):
        print(k * " " + "*" * 6)
        if k == n:
            return
        helper(k+1)
        print(k * " " + "*" * 6)
    helper(0)

print_x(5)