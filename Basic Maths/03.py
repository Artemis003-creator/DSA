# Q3 Check if a number is Palindrome or Not

# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

def pal(n):
    rev = 0
    oiginal = n

    while n > 0:
        digit = n%10
        rev = rev*10 + digit
        n //= 10

    return oiginal == rev

n = int(input())
print(pal(n))