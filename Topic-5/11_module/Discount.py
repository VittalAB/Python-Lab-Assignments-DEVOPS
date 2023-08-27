def discountOffer(i1,i2,i3):
    
    s = sum([i1, i2, i3])
    if i1<0 or i2<0 or i3<0:
        return "Inavlid Input", 0

    
    if s in range(2000, 2501):
        d = 0.4 * s
        return int(d),int(s-d)
    elif s > 2500:
        d = 0.5 * s
        return int(d),int(s-d)
    else:
        return 0,(s)