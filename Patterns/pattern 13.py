# Pattern 13
"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

## Method -1   (By thinking)
def pat13(n):
    for i in range(1,(2*n)):
        if i <= n:
            for j in range(i):
                print("*", end="")
            for j in range((2*n)-(2*i)):
                print(" ",end="")
            for j in range(i):
                print("*", end="")
            print()
        else:
            for j in range((2*n)-i):
                print("*", end="")
            for j in range(i - ((2*n)-i)):
                print(" ",end="")
            for j in range((2*n)-i):
                print("*", end="")
            print()

n = 5
pat13(n)

  
## Method -2  ( By ChatGpt)  --- Saving here for future revision/reference
def pat13(n):
    for i in range(1, 2*n):
        if i <= n:
            stars = i
        else:
            stars = 2*n - i

        spaces = 2*n - 2*stars

        for j in range(stars):
            print("*", end="")

        for j in range(spaces):
            print(" ", end="")

        for j in range(stars):
            print("*", end="")

        print()

n = 5
pat13(n)