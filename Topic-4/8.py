# demo of endswith

def findValue(a, b):
    return a.endswith(b)

if __name__=="__main__":
    s = input()
    ss = input()

    if findValue(s, ss):
        print("YES")
    else:
        print("NO")
        
