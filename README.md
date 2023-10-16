# Fibonacci-Dynamic-Programming
A simple script to understand Dynamic Programming better and see time efficiency of three different algorithms to calculate Fibonacci numbers: Naive, bottom-up and top-down algorithms.

Method 1: Recursive (F(n))

kotlin

Function F(n):
    if n == 0:
        return 0
    else if n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

    This method defines the Fibonacci sequence recursively.
    If n is 0 or 1, it returns the respective base cases.
    Otherwise, it recursively calls itself to calculate F(n) by adding F(n-1) and F(n-2).

Method 2: Iterative (F_b(n))

java

Function F_b(n):
    if n == 0:
        return 0
    else if n == 1:
        return 1
    else:
        a = 0
        b = 1
        n = n - 1
        while n > 0:
            c = a + b
            a = b
            b = c
            n = n - 1
        return b

    This method calculates the Fibonacci sequence iteratively.
    It initializes a and b to 0 and 1, respectively.
    It uses a while loop to iteratively update a and b until it reaches the desired Fibonacci number, which is stored in b.

Method 3: Top-down Dynamic Programming (F_t(n))

arduino

Initialize Fib_num array with -1s of sufficient size

Function F_t(n):
    if Fib_num[n] == -1:
        if n == 0:
            Fib_num[n] = 0
        else if n == 1:
            Fib_num[n] = 1
        else:
            Fib_num[n] = F_t(n-1) + F_t(n-2)
    return Fib_num[n]

    This method uses a top-down dynamic programming approach.
    It initializes an array called Fib_num to store already calculated Fibonacci values.
    If the Fibonacci value for n is not in the array, it calculates it recursively.
    Calculated values are stored in the array for future reference, improving efficiency.

These pseudo-algorithms provide a conceptual understanding of how each method works to compute Fibonacci numbers.
