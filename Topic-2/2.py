if __name__=="__main__":
    while True:
        print("Enter the first value :")
        a = int(input())
        print("Enter the second value :")
        b = int(input())

        print("Enter the choice from menu")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")

        c=int(input())

        if c==1:
            print(f"The value after Addition is {a+b}.")
        elif c==2:
            print(f"The value after Subtraction is {a-b}.")
        elif c==3:
            print(f"The value after Multiplication is {a*b}.")
        else:
            print(f"The value after Division is {a//b}.")

        break
            