# Pattern 10
"""
E
D E
C D E
B C D E
A B C D E


 """
def pat10(n):
    for i in range(n):
        s = "A"
        sw = chr(ord(s) +( n-i-1))
        for j in range(i+1):
            print(f"{sw} ",end="")
            sw = chr(ord(sw)+1)
        print()

pat10(5)