# Exception handling

# Zer division error

if __name__=="__main__":
    fees = int(input("Enter the total fees\n"))
    n = int(input("Enter the no of Students\n"))

    try:
        print(f"Fees to be paid by Individual: {round(fees/n, 2)}")
    except ZeroDivisionError:
        print("Zero Division Error Exception")