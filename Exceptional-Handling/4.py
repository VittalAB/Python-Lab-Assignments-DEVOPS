# Tyoe error

if __name__=="__main__":
    n = input("Enter the number of matches\n")
    s = 0
    print("Enter the scores")
    for i in range(int(n)):

        try:
            s = s + int(input())
        except ValueError:
            print("Type Error Exception")
            exit(0)
    

    print("Batting average: {:.2f}".format(s/int(n)))
