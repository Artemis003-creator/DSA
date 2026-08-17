# Q1 Print Name N times using Recursion

# Problem Description: Given an integer N, write a program to print your name N times. 

def f(name,number,count): 

    if count == number:
        return
    print(name)
    f(name,number, count+1)

name = input("Enter name: ")
number = int(input("Enter N: "))
count = int(input("Enter initial count: "))

f(name,number,count)


