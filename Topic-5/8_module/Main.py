import math as m, math

if __name__=="__main__":
    menu = '''Menu
1.ceil()
2.exp()
3.fabs()
4.factorial()
5.floor()
6.gcd()
7.pow()
8.log2()
9.sqrt()
10.log()
Enter the choice'''

    while True:

        print(menu)

        c = int(input())

        if c == 1:
            n = float(input("Enter the number\n"))
            print(f"The ceil value is  {math.ceil(n)}")
        elif c==2:
            n = int(input("Enter the number\n"))
            print(f"The exponent is  {math.exp(n)}")
        elif c == 3:
            n = int(input("Enter the number\n"))
            print(f"The absolute value is  {m.fabs(n)}")
        elif c==4:
            n = int(input("Enter the number\n"))
            print(f"The factorial of the number is {m.factorial(n)}")
        elif c==5:
            n = float(input("Enter the number\n"))
            print(f"The floor value is  {math.floor(n)}")
        elif c==6:
            n = int(input("Enter the first number\n"))
            n2 = int(input("Enter the second number\n"))
            print(f"The gcd is  {m.gcd(n,n2)}")
        elif c==7:
            n = int(input("Enter the number\n"))
            b = int(input("Enter the base\n"))

            print(f"The power is  {m.pow(n,b)}")
        elif c==8:
            n = int(input("Enter the number\n"))
            print(f'The value of log2 is  {m.log2(n)}')
        elif c==9:
            n = int(input("Enter the number\n"))
            print(f"The square root the given number is {m.sqrt(n)}")
        elif c==10:
            n = int(input("Enter the number\n"))
            b = int(input("Enter the number\n"))
            print(f"The value of log {n} with base {b} is : {m.log(n, b)}")
        else:
            print("Invalid Choice")
            exit(0)

