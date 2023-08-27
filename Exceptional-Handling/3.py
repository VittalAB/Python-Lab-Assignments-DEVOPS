# index error

if __name__=="__main__":
    l = [2,3,1,5,6,7,1]
    print(l)
    print("Enter n")
    n = int(input())
    s=0
    try:
        
        l[n-1]

        for i in range(0, n):
            s=s+l[i]
            
    except IndexError:
        print("Index Value out of range")
    finally:
        if not s:
            pass
        else:
            print("Sum =", s)

        