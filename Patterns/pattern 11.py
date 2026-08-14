# Pattern 11
"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""
def pat11_up(n):
    for i in range(n):
        # symbol
        for j in range(n-i):
            print("*", end="")

        # Space
        for j in range(i*2):
            print(" ", end="")

        # symbol
        for j in range(n-i):
            print("*", end="")

        print()

def pat11_down(n):
    for i in range (1,n+1):
        #symbol
        for j in range(i):
            print("*", end="")

        # Space
        for j in range((2*n)-(2*i)):
            print(" ", end="")

        # Symbol
        for j in range(i):
            print("*", end="")

        print()


n = 5
pat11_up(n)
pat11_down(n)


