from Item import Item 

if __name__=="__main__":

    a = input()
    b = input()
    c = input()
    d = input()
    
    obj = Item(a,b,c,int(d))

    obj.display()