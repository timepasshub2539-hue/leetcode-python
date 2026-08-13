def longestRepeating(s, qc, qi):
    n, s = len(s), list(s); tree = [None]*(4*n)
    def merge(a,b):
        ll = a['ll'] if a['ll']<a['n'] else a['ll']+(b['ll'] if a['rc']==b['lc'] else 0)
        rl = b['rl'] if b['rl']<b['n'] else b['rl']+(a['rl'] if a['rc']==b['lc'] else 0)
        mx = max(a['mx'],b['mx'],(a['rl']+b['ll']) if a['rc']==b['lc'] else 0)
        return {'lc':a['lc'],'rc':b['rc'],'ll':ll,'rl':rl,'mx':mx,'n':a['n']+b['n']}
    def build(nd,l,r):
        if l==r: tree[nd]={'lc':s[l],'rc':s[l],'ll':1,'rl':1,'mx':1,'n':1}; return
        m=(l+r)//2; build(2*nd,l,m); build(2*nd+1,m+1,r); tree[nd]=merge(tree[2*nd],tree[2*nd+1])
    def update(nd,l,r,i,c):
        if l==r: tree[nd]={'lc':c,'rc':c,'ll':1,'rl':1,'mx':1,'n':1}; return
        m=(l+r)//2
        (update(2*nd,l,m,i,c) if i<=m else update(2*nd+1,m+1,r,i,c))
        tree[nd]=merge(tree[2*nd],tree[2*nd+1])
    build(1,0,n-1); ans=[]
    for c,i in zip(qc,qi):
        s[i]=c; update(1,0,n-1,i,c); ans.append(tree[1]['mx'])
    return ans
