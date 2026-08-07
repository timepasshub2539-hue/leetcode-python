def solve(num, t):
    n2=n3=n5=n7=0; x=t
    for p in (2,3,5,7):
        while x % p == 0:
            x //= p
            if p==2: n2+=1
            elif p==3: n3+=1
            elif p==5: n5+=1
            else: n7+=1
    if x != 1:
        return "-1"
    need = (n2,n3,n5,n7)
    if '0' not in num:
        a,b,c,d = need
        for ch in num:
            e2,e3,e5,e7 = DIG[ch]
            a,b,c,d = max(a-e2,0),max(b-e3,0),max(c-e5,0),max(d-e7,0)
        if (a,b,c,d) == (0,0,0,0):
            return num
    L = len(num)
    for i in range(L-1, -1, -1):
        prefix = num[:i]
        if '0' in prefix:
            continue
        a,b,c,d = need
        for ch in prefix:
            e2,e3,e5,e7 = DIG[ch]
            a,b,c,d = max(a-e2,0),max(b-e3,0),max(c-e5,0),max(d-e7,0)
        for dv in range(int(num[i])+1, 10):
            e2,e3,e5,e7 = DIG[str(dv)]
            na,nb,nc,nd = max(a-e2,0),max(b-e3,0),max(c-e5,0),max(d-e7,0)
            if min_len(na,nb,nc,nd) <= L-i-1:
                return prefix+str(dv)+build_suffix((na,nb,nc,nd), L-i-1)
    L += 1
    while min_len(*need) > L:
        L += 1
    return build_suffix(need, L)
