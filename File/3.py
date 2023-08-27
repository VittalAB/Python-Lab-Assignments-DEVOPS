if __name__=="__main__":

    s = 0
    with open("File\sample.txt", "r") as f:
        for n in f:
            s = s + int(n)
        f.close()
    print(f"The sum of the integers in the file sample.txt is:{s}")