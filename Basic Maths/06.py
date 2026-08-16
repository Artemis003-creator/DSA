# Q6 Print all Divisors of a given Number

# Problem Statement: Given an integer N, return all divisors of N.

# All factors of a number can be found till [sq_root(n)] or [i*i <=n]


## Method 1

def all_div(n):
    result = []
    i = 1

    while i*i <=n:
        if n%i == 0 :
            result.append(i)
            if i != n//i:
                result.append((n//i))
        
        i +=1
    return sorted(result)

n = int(input())
print(all_div(n))


## Method 2  --- optimised

def all_div(n):
    smaller = []
    larger = []

    i = 1

    while i*i <=n:
        if n%i == 0 :
            smaller.append(i)
            if i != n//i:
                larger.append((n//i))
        
        i +=1
    result = smaller + larger[::-1]
    return result

n = int(input())
print(all_div(n))