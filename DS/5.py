# dict comparisons 
def double_check(d1:dict, d2:dict) -> bool:
    return all((d1.get(k) == v for k, v in d2.items()))


def dic_insert(s : str, d : dict) -> dict:
    for ele in s:
        try:
            d[ele]+=1
        except:
            d[ele]=1
    return d

if __name__=="__main__":
    s1 = input()
    s2 = input()

    dic1 = {}
    dic2 = {}

    dic1 = dic_insert(s1, dic1)
    dic2 = dic_insert(s2, dic2)

    l1 = list(dic1.values())
    l2 = list(dic2.values())

    if sorted(l1) == sorted(l2):
        if double_check(dic1, dic2):
            print("Strings are matching")
        else:
            print("Strings are not matching")
    else:
        print("Strings are not matching")
    