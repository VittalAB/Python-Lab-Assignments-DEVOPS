if __name__=="__main__":
    marks = int(input("Enter the marks\n"))
    stmt = "The student obtained a x grade"
    if marks < 0:
        print("Invalid Input")
        exit
    if marks in [100]:
        print(stmt.replace('x', 'S'))
    elif marks in range(90, 100):
        print(stmt.replace('x', 'A'))
    elif marks in range(80, 90):
        print(stmt.replace('x', 'B'))
    elif marks in range(70, 80):
        print(stmt.replace('x', 'C'))
    elif marks in range(60, 70):
        print(stmt.replace('x', 'D'))
    elif marks in range(50, 60):
        print(stmt.replace('x', 'E'))
    elif marks < 50:
        print(stmt.replace('x', 'F'))
    else:
        print("Invalid Input")    