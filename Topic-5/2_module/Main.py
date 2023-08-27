from element import element

if __name__=="__main__":
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    e = int(input())
    if element(l, e):
        print("Got It!")
    else:
        print("Sorry!")
