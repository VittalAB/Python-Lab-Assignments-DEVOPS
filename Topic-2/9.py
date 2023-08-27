# To print fibonacci series 


if __name__ == "__main__":
    n = int(input())
    li = [0, 1]
    for i in range(2, n):
        a = li[i-1] + li[i-2]
        li.append(a)
    
    l = " ".join(list(map(str, li)))
    
    print(l)