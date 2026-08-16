# Q7 Check if a number is prime or not

# Problem Statement: Given an integer N, check whether it is prime or not.


def is_prime(n):
    if n < 2:
        return False
    
    i = 2

    # Checking Does n have any factor betwwen 2 to sq_root(n)
    # if yes -- it has more than 2 factors and then NOT a prime no.

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


n = int(input())
print(is_prime(n))
