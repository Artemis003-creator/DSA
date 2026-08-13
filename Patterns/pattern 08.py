# Pattern 8
"""
ord(char)    A single character stringThe integer code point    ord('A') → 65
chr(int)     An integer code pointThe single character string   chr(65) → 'A'

A
AB
ABC
ABCD
ABCDE

"""

def pat8(n):
    for i in range(n):
        sl = "A"
        for j in range(i+1):
            print(sl,end="")
            sl = chr(ord(sl)+1)
        print()

pat8(5)