# NameError
# ZeroDivisionError
if __name__=="__main__":

    try : 
        print("Enter the Income of the Restaurant per month")
        i = int(input())
        print("Enter the No of Waiters")
        n = int(input())
        print("Enter the salary allocated for the waiters")
        s = int(input())
        profit = "{:.2f}".format(i-s)
        salary = "{:.2f}".format(s//n)
        print(f"Profit: {profit}")
        print(f"Salary per Waiter: {salary}")
    except:
        print("Exception has been occured")
        exit(0)




