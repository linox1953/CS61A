def printer_rev(n):
    print('*' * n)
    if n == 1:
        return 
    printer_rev(n-1)
    print('*' * n)

def printer_cor(n):
    def printer(k):
        print('*' * k)
        if n == k:
            return
        printer(k+1)
        print('*' * k)
    printer(1)

print("输入倒序的n:")
printer_rev(int(input()))
print("输入正序的n:")
printer_cor(int(input()))