def tribo(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return 1

    return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)


print(tribo(25))
