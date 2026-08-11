def up(x):
    for i in range(x):
        for j in range(x-i-1):
            print(" ",end="")
        for j in range((2*i)+1):
            print("*",end="")
        for j in range(x-i-1):
            print(" ",end="")
        print()
def down(x):
    for i in range(x):
        for j in range(i):
            print(" ",end="")
        for j in range((2*x)-(2*i)-1):
            print("*",end="")
        for j in range(i):
            print(" ",end="")
        print()


x = 5
up(x)
down(x)