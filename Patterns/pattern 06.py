# Pattern 6
"""
1        1
12      21
123    321
1234  4321
1234554321
"""

def pat6(n):
    for i in range(1,n+1):
        num = 1
        for j in range(i):
            print(num,end="")
            num +=1
        for j in range((2*n)-(2*i)):
            print(" ",end="")
        for j in range(i):
            num -=1
            print(num,end="")
        print()

        
pat6(5)