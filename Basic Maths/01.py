# Q1 Count digits in a number

# Problem Statement: Given an integer N, return the number of digits in N. 

def count_num(n):
    if n ==0:
        return 1

    n = abs(n)
    count = 0

    while n > 0:
        n = n//10
        count +=1
        
    return count 

n = int(input())
print(count_num(n))