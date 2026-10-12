def printNumbers(i, n):
    if i > n:
        return
    print(i, end=" ")
    printNumbers(i + 1, n)


printNumbers(1, 50)