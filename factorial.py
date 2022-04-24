# A function to calculate the factorial of any whole number

def fact(n):
    # Base case
    if n == 1:
        return 1

    # Recursive case
    if n == 0:
        return 1
    return n * fact(n-1)