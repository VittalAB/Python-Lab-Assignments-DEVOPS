if __name__=="__main__":
    display = '''1.Insert
2.Reverse
3.Display multiple times
4.Concatenate two lists
5.Sort the elements in the list in ascending order'''

    print("Enter the  list")
    l = input()

    l = l[1:]
    l = l[:len(l)-1]
    l = l.split(',')
    l = list(map(int, l))

    arr = l
    while True:

        print(display)

        c = int(input("Enter your choice:\n"))

        if c == 1:
            print("How many elements do you want to insert :")
            n = int(input())
            for i in range(n):
                print("Enter the element to insert")
                arr.append(int(input()))

            print("Do you want to continue?(Yes/No)")
            res = input()

            if res == 'Yes':
                continue
            else:
                exit()
        elif c==2:
            rev = reversed(arr)
            print(f"Reversed List : {list(rev)}")
            print("Do you want to continue?(Yes/No)")
            res = input()

            if res == 'Yes':
                continue
            else:
                exit()
        elif c == 3:
            # arr = arr + arr
            print("Enter the count")
            n = int(input())
            t = []
            for i in range(n):
                t = t + arr
            print(f"{n} times {t}")
            print("Do you want to continue?(Yes/No)")
            res = input()

            if res == 'Yes':
                continue
            else:
                exit()
        elif c == 4:
            print("Enter new list")
            
            l = input()

            l = l[1:]
            l = l[:len(l)-1]
            l = l.split(',')
            l = list(map(int, l))
          
            print(f"merged list : {arr+l}")

            print("Do you want to continue?(Yes/No)")
            res = input()

            if res == 'Yes':
                continue
            else:
                exit()
        elif c == 5:
            print(f"Sorted List : {sorted(arr)}")
            # print("Do you want to c")
            print("Do you want to continue?(Yes/No)")
            res = input()

            if res == 'Yes':
                continue
            else:
                exit()
            
