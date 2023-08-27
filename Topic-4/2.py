# demo of args

def findMinimum(*args):
    return min(args)

if __name__=="__main__":
    display = '''Menu
1. Minimum of 3
2. Minimum of 4
3. Minimum of 5
'''
    print(display)
    c = int(input())

    if c == 1:
        print("Enter 3 values")
        a = int(input())
        b = int(input())
        c = int(input())
        print(f"Minimum of ({a}, {b}, {c}) is {findMinimum(a, b, c)}")
    elif c == 2:
        print("Enter 4 values")
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        print(f"Minimum of ({a}, {b}, {c}, {d}) is {findMinimum(a, b, c, d)}")
    elif c == 3:
        print("Enter 5 values")
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        e = int(input())
        print(f"Minimum of ({a}, {b}, {c}, {d}, {e}) is {findMinimum(a, b, c, d, e)}")
