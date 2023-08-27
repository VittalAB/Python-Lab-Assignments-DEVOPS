if __name__=="__main__":
    c = 0
    with open("File\input.txt", "r") as f:
        for l in f:
            c=c+1
        f.close()
        print(f"The file has {c} lines")
