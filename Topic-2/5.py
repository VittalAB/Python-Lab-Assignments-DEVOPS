if __name__=="__main__":
    print("Enter the value :")
    n = input()
    li = list(map(int, list(n)))
    s = 0
    i = 0
    while i < len(li):
        s += li[i]
        i += 1
    print(f"Sum of digits in {''.join(n)} is {s}")