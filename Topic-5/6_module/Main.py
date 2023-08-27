import calendar

if __name__=="__main__":
    menu = '''Menu
1.calendar()
2.firstweekday()
3.isleap()
4.leapdays()
5.month()
6.monthrange()
7.prcal()
8.prmonth()
9.setfirstweekday()
10.weekday()'''

    while True:
        print(menu)
        print("Enter the choice")
        c = int(input())

        if c==1:
            print("Enter the year")
            y = int(input())
            print(f"The calender of year {y} is : ")
            print(calendar.calendar(y))
        elif c==2:
            print(f"The starting day number in calendar is : {calendar.firstweekday()}")
        elif c==3:
            y = input("Enter the year\n")
            y = int(y)

            if calendar.isleap(y):
                print("The year is leap")
            else:
                print("The year is not leap")
        elif c==4:
            s = int(input("Enter the start date\n"))
            e = int(input("Enter the end date\n"))

            print(f"The leap days between {s} and {e} are : {calendar.leapdays(s, e)}")
        elif c==5:
            y = int(input("Enter the year\n"))
            m = int(input("Enter the month\n"))

            print(f"The month {m}th of {y} is :")
            print(calendar.month(y, m))
        elif c==6:
            y = int(input("Enter the year\n"))
            m = int(input("Enter the month\n"))
            print(f"The start week number and no. of days of month : {calendar.monthrange(y, m)}")
        elif c==7:
            y = int(input("Enter the year\n"))
            print(f"The calendar of {y} is : ")
            calendar.prcal(y)
        elif c==8:
            y = int(input("Enter the year\n"))
            m = int(input("Enter the month\n"))

            print(f"The {m}th month of {y} is : ")
            if m not in range(1, 13):
                print("Invalid Choice")
                exit(0)

            calendar.prmonth(y, m)

        elif c==9:
            w = int(input("Enter the weekday number\n"))
            if w not in range(0, 7):
                print("Invalid Choice")
                exit(0)

            calendar.setfirstweekday(w)
            print(f"The new week day number is : {calendar.firstweekday()}")
        
        elif c==10:
            d = int(input("Enter the date\n"))
            m = int(input("Enter the month\n"))
            y = int(input("Enter the year\n"))
            print(f"The day number is : {calendar.weekday(y, m, d)}")
        
        else:
            print("Invalid Choice")
            exit(0)