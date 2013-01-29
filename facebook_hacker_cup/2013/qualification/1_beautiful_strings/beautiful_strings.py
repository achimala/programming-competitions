def f(s):
    m = {}
    for c in (c for c in s.lower() if c.isalpha()):
        m[c] = m.setdefault(c, 0) + 1
    return sum(m[c] * b for b, c in zip(range(26, 0, -1), sorted(m, key=lambda c: m[c], reverse=True)))

with open("beautiful_strings.in", "r") as inp:
    for i, s in enumerate(inp.read().strip().split("\n")[1:]):
        print "Case #{}: {}".format(i+1, f(s))

# one line:
# print "\n".join(map(lambda(i,s):(lambda m:map(lambda c:(lambda x:x.insert(0,x[0]+1))(m.setdefault(c,[0])),filter(lambda c:c.isalpha(),s.lower()))and"Case #%d: %s"%(i+1,sum(m[c][0]*b for b,c in zip(range(26,0,-1),sorted(m,key=lambda c:m[c][0])[::-1]))))({}),enumerate(open("beautiful_strings.in").read().strip().split("\n")[1:])))