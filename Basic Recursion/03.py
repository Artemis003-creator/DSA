# Q3 Print N to 1 using Recursion

# Problem Description: Given an integer N, write a program to print numbers from N to 1

## Method 1 - Forward recursion

def f(number):
    if number <1:
        return

    print(number)
    f(number-1)

number = int(input("Enter N: "))
f(number)

##  Method 2 - Backward recursion

def f(n, current):
    if current > n:
        return

    f(n, current + 1)
    print(current)


n = int(input("Enter N: "))
f(n, 1)