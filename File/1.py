if __name__=="__main__":

    with open("File\output.txt", "w") as w:
        with open("File\input.txt", "r") as f:
            for line in f:
                w.writelines(line.title())
            f.close()
        w.close()
