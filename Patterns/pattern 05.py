# Pattern 5
"""
1
01
101
0101
10101
"""

def pat5(n):
    for i in range(n):
        if i%2 == 0:
            swap = 1
        else:
            swap = 0
        for j in range(i+1):
            print(swap,end="")
            swap = 1 - swap
        print()

pat5(5)