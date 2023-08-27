# ymmetric difference

if __name__=="__main__":

    s = set(map(int, input().split(','))).symmetric_difference(set(map(int, input().split(','))))

    if len(s) > 0:
        print(s)
    else:
        print("invalid set")