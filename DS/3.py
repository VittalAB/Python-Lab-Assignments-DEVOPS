if __name__=="__main__":
    print("Enter the tuple")

    tup = tuple(map(int, input().split(',')))

    menu = '''1.Print first and last element

2.Minimum element

3.Sum of the elements

4.Print multiple times

Enter your option'''


    while True:

        print(menu)

        c = int(input())

        if c == 1:
            ans = f'''Elements :  {tup[0]} {tup[len(tup)-1]}

Do you want to continue?(Yes/No)'''
            print(ans)

            res = input()

            if res == 'No':
                break

        elif c==2:
            ans = f'''Minimum element :  {min(tup)}

Do you want to continue?(Yes/No)'''
            
            print(ans)

            res = input()

            if res == 'No':
                break
        elif c==3:
            ans = f'''Sum of the elements :  {sum(tup)}

Do you want to continue?(Yes/No)'''
            print(ans)

            res = input()

            if res=='No':
                break
        else:
            print("Enter the count")
            k = int(input())
            ans = f'''{k} times tuple :  {tup*k}

Do you want to continue?(Yes/No)'''
            
            print(ans)

            res = input()

            if res=='No':
                break