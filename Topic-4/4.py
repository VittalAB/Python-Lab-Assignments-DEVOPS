# Simplest fraction
import math

def printValue(num, den):
    if num%den == 0:
        return num//den
    else:
        if num > den:
            a = num // den
            b = num % den
            return f'{a} {b}/{den}'
        else:
            gcd = math.gcd(num, den)
            return f'{num//gcd}/{den//gcd}'
    
if __name__=="__main__":
    a = int(input())
    b = int(input())

    if a>0 and b>0:
        print(printValue(a, b))
    else:
        print("Invalid Input")
        