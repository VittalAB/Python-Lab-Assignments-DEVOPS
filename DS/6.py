# # set operations

def modify(s:str):
    l = s.split(',')
    l = [str(ele) for ele in l]

    return str(l)

# s = "app,ban,org"

# print(modify(s))

if __name__=='__main__':

    a = input("Enter the elements of set1\n")
    b = input("Enter the elements of set2\n")

    a, b = set(a.split(',')), set(b.split(','))

    print("Enter your choice")
    display = '''1.Add
2.Remove
3.Difference
4.intersection
Enter your choice'''
    sub_display = '''1.set1
2.set2'''

    print(display)

    c = int(input())

    if c == 1:
        print(sub_display)

        sc = int(input())

        if sc == 1:
            ele = input("Enter the item to be added\n")

            a.add(ele)
            t = list(a)
            t.sort()
            pt = ','.join(t)
            
            pt = modify(pt)

            print("set(" + pt + ")")
            
        elif sc == 2:
            b.add(input("Enter the item to be added\n"))
            t = list(b)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        else:
            print("invalid choice")

    elif c == 2:
        print(sub_display)

        sc = int(input())

        if sc == 1:
            a.remove(input("Enter the item to be removed\n"))
            t = list(a)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        elif sc == 2:
            b.remove(input("Enter the item to be removed\n"))
            t = list(b)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        else:
            print("invalid choice")
    elif c == 3:
        print(sub_display)

        sc = int(input())

        if sc == 1:
            a=a.difference(b)
            t = list(a)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        elif sc == 2:
            b=b.difference(a)
            t = list(b)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        else:
            print("invalid choice")
    elif c == 4:
        print(sub_display)

        sc = int(input())

        if sc == 1:
            a=a.intersection(b)
            t = list(a)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            print("set(" + pt + ")")

        elif sc == 2:
            b=b.intersection(a)
            t = list(b)
            t.sort()
            pt = ','.join(t)
            pt = modify(pt)
            

            print("set(" + pt + ")")
        else:
            print("invalid choice")




            # pt = modify(pt)