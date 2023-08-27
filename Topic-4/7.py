import math

def findValue(a, b):
    return math.gcd(a, b) 

if __name__=="__main__":
    a = int(input())
    b = int(input())
    print(findValue(a, b))