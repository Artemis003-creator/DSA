# Pattern 12
"""
****
*  *
*  *
****
"""

def pat12(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == (n-1):
                print("*", end="")

            else:
                if j == 0 or j == (n-1):
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

n = 4
pat12(n)