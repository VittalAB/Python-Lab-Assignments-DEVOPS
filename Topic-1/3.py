if __name__=="__main__":
    days = int(input())
    wages = int(input())
    fine = int(input())
    total = int(input())
    temp  = fine * days
    t1 = wages + fine
    t2  = total + temp
    ans = t2//t1
    print(days - ans)

