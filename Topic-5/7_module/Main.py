import datetime

def days_between(d1, d2):
    return abs(d2 - d1).days


if __name__=="__main__":
    menu = '''Menu
1.date()
2.strftime()
3.Difference between 2 dates
4.Creating user datetime()
5.dir()
6.strptime()
Enter the choice'''

    while True:
        print(menu)

        c = int(input())

        if c==1:
            print("Enter the year")
            y = int(input())
            m = int(input("Enter the month\n"))
            d = int(input("Enter the date\n"))
            s = datetime.date(y,m,d)
            s = str(s)
            s1 = s[0:4] + " - "
            s2 = s[5:7] + " - "  
            s3 = s[8:]
            print(f"The represented date is : {s1+s2+s3}")

        elif c==2:
            print("Enter the year")
            y = int(input())
            m = int(input("Enter the month\n"))
            d = int(input("Enter the date\n"))
            obj = datetime.datetime(y, m ,d)

            print(obj.strftime("%B"))

        elif c==3:
            print("Enter the year1")
            y = int(input())
            m = int(input("Enter the month1\n"))
            d = int(input("Enter the date1\n"))
            print("Enter the year2")
            y2 = int(input())
            m2 = int(input("Enter the month2\n"))
            d2 = int(input("Enter the date2\n"))

            d1 = datetime.date(y, m, d)
            d2 = datetime.date(y2, m2, d2)

            diff = days_between(d1, d2)

            print(f"Difference is  {diff} days, 0:00:00")
        
        elif c==4:
            print("Enter the year")
            y = int(input())
            print("Enter the month")
            m = int(input())
            print("Enter the date")
            d = int(input())

            d = datetime.datetime(y, m, d).strftime("%Y-%m-%d %H:%M:%S")

            print(f"The created date and time is : {d}")
        
        elif c==5:
            print(dir(datetime.datetime))
        elif c==6:
            import time

            time_string = "21 July, 2025"
            result = time.strptime(time_string, "%d %B, %Y")

            print(result)
        else:
            print("Invalid Choice")
            exit(0)