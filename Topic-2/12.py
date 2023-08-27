
if __name__=="__main__":

    r = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    count = 0

    while r>0:

        if a==25:
            r=r+20
        
        r=r-1

        count+=1

        if r==0:
            break

        if b==120:
            r+=80
        r=r-1

        count+=1

        if r==0:
            break

        if c==12:
            r=r+8
        
        r=r-1

        count+=1

        if r==0:
            break

        a=a+1
        b=b+1
        c=c+1

    print(f"Peter plays {count} times before going broke")
