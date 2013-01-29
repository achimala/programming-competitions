def answer(a, b, c, r, n, k):
    m = [a]
    mcontains = {a: 1}
    def inm(x):
        return mcontains.setdefault(x, 0) > 0
    def addm(x):
        m.append(x)
        mcontains[x] = mcontains.setdefault(x, 0) + 1
    def popm():
        m0 = m.pop(0)
        mcontains[m0] -= 1
        return m0
    
    bestnext = 0 if a > 0 else 1
    
    for i in range(1, k):
        new = (b * m[-1] + c) % r
        addm(new)
        while inm(bestnext):
            bestnext += 1
    
    for i in range(k):
        m0 = popm()
        addm(bestnext)
        if not inm(m0):
            bestnext = min(m0, bestnext + 1)
        else:
            bestnext += 1
        while inm(bestnext):
            bestnext += 1
    
    addm(bestnext)
    return m[n % (k+1)]

with open("find_the_min.in", "r") as inp:
    lines = inp.read().strip().split("\n")
    for i in range(1, len(lines), 2):
        print "Case #{}: {}".format(i/2+1, answer(*map(int, (lines[i+1] + ' ' + lines[i]).split(' '))))