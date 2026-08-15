# Q2 Reverse Digits of A Number

# Problem Statement: Given an integer N return the reverse of the given number.
# Note: If a number has trailing zeros, then its reverse will not include them. For e.g , reverse of 10400 will be 401 instead of 00401. 

def rev(n):
    sign = -1 if n < 0 else 1    

    n = abs(n)
    result = 0

    while n > 0:
        digit = n%10
        result = result*10 + digit
        n = n//10

    return sign*result    


n = int(input())
print(rev(n))