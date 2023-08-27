from Discount import *

if __name__=="__main__":
    i1 = int(input())
    i2 = int(input())
    i3 = int(input())

    
    d_amt, payable = discountOffer(i1, i2, i3)

    if type(d_amt) == str:
        print("Invalid Input")
        exit(0)

    if d_amt:
        print(f"Discount of Rs.{d_amt}")
        print(f"Total amount to be paid is Rs.{payable}")
    else:
        print(f"Total amount to be paid is Rs.{payable}")
