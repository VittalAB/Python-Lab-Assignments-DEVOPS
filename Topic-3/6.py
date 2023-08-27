# trim on both sides and capitalize second word


if __name__=="__main__":
    s = input("Enter the input string\n")
    s = s.rstrip()
    s = s.lstrip()
    l = s.split(' ')
    su =  ''
    for i in range(1, len(l)):
        su= su + ' ' + l[i].upper()
    print('The processed string is',l[0] + su)