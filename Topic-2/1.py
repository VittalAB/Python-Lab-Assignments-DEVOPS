if __name__=="__main__":

    a = int(input())
    b = int(input())
    c = int(input())

    if a > b and a > c:
        print(f"{a} is the maximum number")
    elif b > c and b >a:
        print(f"{b} is the maximum number")
    else:
        print(f"{c} is the maximum number")
        