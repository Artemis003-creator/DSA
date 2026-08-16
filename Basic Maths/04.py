
# Q4 Find GCD of two numbers

# Problem Statement: Given two integers N1 and N2, find their greatest common divisor. (a,b > 0)



def gcd(a,b):

    while a >0 and b > 0:
        if a>b :
            a = a%b
        else:
            b = b%a

    if a == 0:
        return b
    else:
        return a

a  = int(input())
b  = int(input())
print(gcd(a,b))