def display(dic : dict):
    for k, v in dic.items():
        print(f"{k} - {v}")

if __name__=="__main__":
    menu = '''1.Add element to the dictionary

2.Display the length of the dictionary

3.Update the element

4.Clear dictionary

5.Display items

6.Exit

Enter your choice'''

    dic= {} 

    while True:

        print(menu)

        c = int(input())

        if c==1:
            print("Enter the number of elements do you want to enter :")
            n = int(input())



            for i in range(n):
                print("Enter the item :")
                i = input()
                print("Enter the price for the item :")
                p = int(input())

                dic[i] = p

            res = input("Do you want to continue?(Yes/No)\n")

            if res=='No':
                break

        elif c==2:
            print(f"Length is :  {len(dic)}")
            res = input("Do you want to continue?(Yes/No)\n")

            if res=='No':
                break
        elif c==3:
            print("Enter the item to update :")
            i = input()
            print("Enter the new price for the item :")
            p = int(input())

            # if len(dic)==0:
            #     dic = {}

            dic[i] = p

            res = input("Do you want to continue?(Yes/No)\n")

            if res=='No':
                break
        elif c==4:
            dic.clear()

            res = input("Do you want to continue?(Yes/No)\n")

            if res=='No':
                break
        elif c==5:
            display(dic)
            res = input("Do you want to continue?(Yes/No)\n")

            if res=='No':
                break
        else:
            exit(0)
