# default args in python

def calculateArea(len=50, b=40):
    return len*b

if __name__=="__main__":
    n = int(input("Enter the number of rooms\n"))
    display = '''Menu
Enter 1 for standard length and breadth
Enter 2 for standard breadth alone
Enter 3 for non standard length and breadth'''

    for i in range(n):
        print(f"Enter room {i+1} details")
        print(display)
        c = int(input())

        if c == 1:
            print(f"Length of the room is 50 and breadth of the room is 40")
            print(f"Area of room {i+1} is {calculateArea()}")
        elif c == 2:
            print("Enter length of the room")
            l = int(input())
            print(f"Length of the room is {l} and breadth of the room is 40")
            print(f"Area of room {i+1} is {calculateArea(l)}")
        else:
            l = int(input("Enter length of the room\n"))
            b = int(input("Enter breadth of the room\n"))

            print(f"Length of the room is {l} and breadth of the room is {b}")

            print(f"Area of room {i+1} is {calculateArea(l, b)}")
        
