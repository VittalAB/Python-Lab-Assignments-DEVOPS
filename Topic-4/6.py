# Best programmer get number od=f divisors


def findType(n):
    s = 0

    for i in range(1, n):
        if n%i==0:
            s+=i   
    
    if s==n:
        return 0
    elif n > s:
        return 1
    else:
        return -1
    
if __name__=="__main__":
    n = int(input())

    res = findType(n)

    if res == 0:
        print(f"{n} is perfect number")
    elif res == 1:
        print(f"{n} is deficient number")
    else:
        print(f"{n} is abundant number")


