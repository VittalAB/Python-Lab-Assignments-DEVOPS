# List comparison

if __name__=="__main__":
    print("Enter the length of the list:")
    n = int(input())

    print("Enter the elements for first list:")
    l1 = input().split()
    l1.sort()
    print("Enter the elements for second list:")
    l2 = input().split()
    l2.sort()

    if l1 > l2:
        print("First list is bigger than Second list")
    elif l1 < l2:
        print("Second list is bigger than First list")
    else:
        print("Both list are equal")