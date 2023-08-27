# list of prime numbers in given range
import math

def check_prime(n):
    is_prime = True
    
    if n==2:
        return is_prime
    i = 2

    while i <= int(math.sqrt(n)+1):
        if n%i == 0:
            is_prime = False
        i+=1
    return is_prime


def prime_numbers(a, b):
    ans  = []
    for i in range(a, b+1):
        if check_prime(i):
            ans.append(i)
    return ans


if __name__=="__main__":

    a = int(input())
    b = int(input())
    stmt = "No prime numbers found in the range"
    ans = prime_numbers(a, b)
    if a == b or a > b:
        print(stmt)

    for ele in ans:
        print(ele, end=" ")