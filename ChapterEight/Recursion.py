def factorial(n):  # Recursive
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)


n = int(input("Enter any number: "))
print("Factorial of a number: ", factorial(n))
