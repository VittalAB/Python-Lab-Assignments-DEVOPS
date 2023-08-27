if __name__=="__main__":
    a = int(input())
    b = int(input())

    lcm = 60

    if b <= 60:
        print(f"All positions change in year {b}")
    else:
        while a <= b:
            print(f"All positions change in year {a}")
            a = a + 60