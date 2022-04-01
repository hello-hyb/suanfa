def recursion(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recursion(n - 1)


print(recursion(4))
