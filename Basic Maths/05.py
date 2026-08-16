# Q5 Check if a number is Armstrong Number or not

# Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

def is_arm(n):

    if n == 0:
         return True

    total = 0
    count = 0
    arm1 = arm2 = n

    while arm1 >0:
            count += 1
            arm1 //=10

    while arm2 >0:
        digit = arm2%10
        total += (digit**count)
        arm2 //=10

    return total == n


n = int(input())
print(is_arm(n))

