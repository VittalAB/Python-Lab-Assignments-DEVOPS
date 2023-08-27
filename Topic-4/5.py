# airthmatic operations using functions


def arithmeticOperation(a, b):
    print(f'Addition : {a+b}')
    print(f'Subtraction : {a-b}')
    print(f'Multiplication : {a*b}')
    print(f'Division : {a//b}')


if __name__=="__main__":
    a = int(input("Enter a\n"))
    b = int(input("Enter b\n"))
    arithmeticOperation(a, b)

