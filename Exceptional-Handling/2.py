# Value error


def modify(s : str):
    l = len(s[s.index('.'):])
    if l!=3:
        s = s + '0'
    else:
        return s
    return s

if __name__=="__main__":
    
    try:
        a = int(input("Enter number 1\n"))
        b = int(input("Enter number 2\n"))
    except ValueError:
        print("Invalid Value")
        exit()

    try:
        s = str(a/b)
        s = modify(s)

        print(s)
    except ZeroDivisionError:
        print("Divide By Zero Error")

