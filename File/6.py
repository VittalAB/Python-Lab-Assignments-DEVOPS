if __name__=="__main__":

    with open("File\data.txt", "r") as f:

        for line in f:
            print(line.split())
        
    