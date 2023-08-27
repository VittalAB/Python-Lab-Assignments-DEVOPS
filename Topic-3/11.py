# string built in functions

if __name__=="__main__":
    display = '''Menu
1.Index of first occurrence of substring
2.Split by length
3.Exit'''
    while True:
        print(display)
        c = int(input("Enter your choice\n"))
        if c == 1:
            s = input("Enter the string\n")
            v = input("Enter the value\n")
            print(f"The index of first occurrence of substring is : {s.find(v)}")
        elif c == 2:
            s = input("Enter the string\n")
            k = int(input("Enter the length of the chunk\n"))
            print([s[i:i+k] for i in range(0, len(s), k)])
        else:
            exit()