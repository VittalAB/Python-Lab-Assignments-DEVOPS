# String built in poperties 


if __name__=="__main__":
    display = '''Menu
1.The last occurrence of specified value in a string
2.Join the string
3.The first occurrence of specified value in a string
4.Exit'''

    while True:
        print(display)

        c = int(input("Enter your choice\n"))
        
        if c == 1:
            s = input("Enter the string\n")
            v = input("Enter the value\n")

            print(f"The last occurrence of specified value is {s.rfind(v)}")
        elif c == 2:
            s1 = input("Enter the first string\n")
            s2 = input("Enter the second string\n")
            s = s2.join(s1.split())
            print(f"The new formed string is {s}")
        elif c == 3:
            s = input("Enter the string\n")
            v = input("Enter the value\n")

            print(f"The first occurrence of specified value is {s.find(v)}")
        elif c==4:
            exit()
            