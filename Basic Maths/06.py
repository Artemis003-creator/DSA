# Q6 Print all Divisors of a given Number

# Problem Statement: Given an integer N, return all divisors of N.

# All factors of a number can be found till [sq_root(n)] or [i*i <=n]

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