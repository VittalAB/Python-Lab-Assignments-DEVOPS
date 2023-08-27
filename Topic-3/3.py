def check(a, b):
    a, b = str(a), str(b)

    if a == b:
        return f"{b} IS CORRECT"
    else:
        if len(a) != len(b):
            return f"{b} IS WRONG"
        else:
            c=0
            for ele in zip(a, b):
                if ele[0] != ele[1]:
                    c=c+1
            if c <= 2:
                return f"{b} IS ALMOST CORRECT"
            else:
                return f"{b} IS WRONG"


if __name__=="__main__":
    a = input()
    b = input()

    print(check(a, b))