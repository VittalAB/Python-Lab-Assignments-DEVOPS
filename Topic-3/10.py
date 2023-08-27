# String built in functions
def get_indices(s, sub):
    ind = []

    s, sub = str(s), str(sub)
    i = s.find(sub)

    while i!=-1:
        ind.append(i)
        i = s.find(sub, i+1)
    # ind = list(map(str, ind))
    return ind

if __name__=="__main__":
    display = '''Menu
1.Counting character sequence in string
2.Index of substring in string
3.Repeating K times
4.Exit'''

    while True:

        print(display)

        c = int(input("Enter your choice\n"))

        if c == 1:
            print("Enter the string")
            s = input()
            sub = input("Enter the substring\n")

            print(f"The count of the character sequence in string is : {s.count(sub)}")
        elif c == 2:
            print("Enter the string")
            s = input()
            if s.startswith(sub):
                pass
            sub = input("Enter the substring\n")
            print(f"The start indices of the substrings are : {get_indices(s, sub)}")
        elif c == 3:
            print("Enter the string")
            s = input()
            v = int(input("Enter the value of K\n"))

            print(f"The original string : {s}")
            s=s*v
            print(f"String after performing repetition : {s[:10]}")
        else:
            exit()