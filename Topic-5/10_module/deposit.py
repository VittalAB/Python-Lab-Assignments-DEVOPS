def depositWithdraw(s):
    s = str(s)
    ele = s.split(',')

    D = []
    W = []

    for e in ele:
        if 'D' in e:
            D.append(int(e[2:]))
        else:
            W.append(int(e[2:]))
    
    return sum(D) - sum(W)