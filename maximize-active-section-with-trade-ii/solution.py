i0=bisect.bisect_left(A, l+1)
i1=bisect.bisect_right(B, r-1)-1
if i0>i1: ans=total
else:
    def gain(i):
        a,b,c,d,bs=cand[i]
        return (a-max(c,l))+(min(d,r)-b)
    g=max(gain(i0),gain(i1),rmax(i0+1,i1-1))
    ans=total+g
