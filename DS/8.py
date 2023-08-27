# split string

if __name__=="__main__":
    s = input()

    l = s.split(',')

    dic = {}
    dic[0] = 'Door-no'
    dic[1] = 'Street'
    dic[2] = 'Area'
    dic[3] = 'City'
    dic[4] = 'State'
    dic[5] = 'Zipcode'
    dic[6] = 'Country'

    for i in range(len(l)):
        print(f"{dic[i]}: {l[i]}") 
        