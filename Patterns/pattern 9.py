# Pattern 9
"""
   A   
  ABA  
 ABCBA 
ABCDCBA
"""

def pat9(n):
    for i in range(n):
        sl = "A"

        for j in range(n-i-1):
            print(" ",end="")

        for j in range(i+1):
            print(sl,end="")
            sl = chr(ord(sl)+1)
        sl = chr(ord(sl)-2)

        for j in range(i):
            print(sl,end="")
            sl = chr(ord(sl)-1)

        for j in range(n-i-1):
            print(" ",end="")
           
        print()

pat9(4)
