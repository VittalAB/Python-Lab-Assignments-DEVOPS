if __name__=="__main__":

    n = input()
    if n.endswith('0'):
        while n.endswith('0'):
            n = n[:len(n)-1]
        
        if n[len(n)-1]=='0':
            n=n[:len(n)-1]
        print(n[::-1])
    else:
        print(n[::-1])
    

