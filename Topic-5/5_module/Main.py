# use of the random module
import random

random.seed(2)

if __name__=="__main__":
    menu = '''Menu
1.random()
2.randint()
3.randrange()
4.choice(seq)
5.sample()
6.shuffle()
7.uniform()'''

    while True:
        print(menu)
        n = int(input("Enter your choice\n"))

        if n==1:
            print("Printing random number using random.random()")
            print(random.random())
        elif n==2:
            print("Enter the start range")
            a = int(input())
            print("Enter the stop range")
            b = int(input())
            print(f"Random integer is {random.randint(a, b)}")
        elif n==3:
            print("Enter the start range")
            a = int(input())
            print("Enter the stop range")
            b = int(input())
            print("Enter the step count")
            c = int(input())
            
            print(f"Random integer is {random.randrange(a, b, c)}")

        elif n==4:
            print("Enter the number of elements inside the list")
            n = int(input())

            print("Enter the element")

            l = [int(input()) for i in range(n)]

            print(f"Random element from list: {random.choice(l)}")
        elif n==5:
            print("Enter the number of elements inside the list")
            n = int(input())

            print("Enter the element")

            l = [int(input()) for i in range(n)]
            l = random.sample(l, 2)
            l = list(map(str, l))
            print(f"Random element from list: {l}")
        elif n==6:
            print("Enter the number of elements inside the list")
            n = int(input())

            print("Enter the element")

            l = [int(input()) for i in range(n)]
            random.shuffle(l)
            print(f"Printing shuffled list  ")
            print(f"{l}")

        elif n==7:
            print("Enter the start range")
            a = input()
            print("Enter the stop range")
            b = input()
            print("floating point within given range")
            print(random.uniform(float(a), float(b)))

        else:
            print("Invalid Choice")  
            exit(0)          


