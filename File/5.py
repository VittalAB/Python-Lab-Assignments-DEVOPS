if __name__=="__main__":
    f1 = open("File\input.txt", "r")
    data = f1.read()
    f2 = open("File\output_c.txt", "w")
    f2.write(data)

    f1.close()
    f2.close()