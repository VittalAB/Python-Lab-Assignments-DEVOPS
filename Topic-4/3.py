# Expression eval

def calculate(x, n):
    if n == 0:
        return f"The result is\n1"
    elif n < 0:
        return "Invalid Input"
    s = 0
    for i in range(1, n+1):
        s+=(x**i)
    return f"The result is\n{s}"

if __name__=="__main__":
    x = int(input("Enter the value of x\n"))
    n = int(input("Enter the value of n\n"))
    print(calculate(x, n))