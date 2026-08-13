# Pattern 4
"""
*
**
***
****
*****
*****
****
***
**
*
"""


def pattern4(n):
    for i in range(2*n):
        if i < n:
            for j in range(i+1):
                print("*",end="")
            print()
        else:
            for j in range((2*n)-i):
                print("*",end="")
            print()


pattern4(5)