if __name__=="__main__":
    s = ""
    with open("File\input.txt", "r") as f:
        d = f.read()
        d = d[::-1]
        f.close()

    o = open("File\o.txt", "w")
    o.write(d)
    o.close()