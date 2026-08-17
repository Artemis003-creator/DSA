# Q2 Print 1 to N using Recursion

# Problem Description: Given an integer N, write a program to print numbers from 1 to N. 


# Method 1 -- forward recursion
def f(number, current):
    if current> number:
        return

    print(current)
    f(number, current+1)

number = int(input(" Enter N: "))
current = int(input(" Enter current: "))

f(number, current)


# Method 1 -- Backward recursion
def f2(number):
    if number <1:
            return

    f2(number-1)
    print(number)


number = int(input(" Enter N: "))


f2(number)
