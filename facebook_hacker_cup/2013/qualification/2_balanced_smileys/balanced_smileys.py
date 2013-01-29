def is_balanced(s):
    depths = set([0])
    wascolon = False
    for c in s:
        old = set([x for x in depths])
        if c == '(':
            depths = set(map(lambda d: d+1, depths))
        if c == ')':
            depths = set(map(lambda d: d-1, depths))
        if c in '()' and wascolon:
            depths |= old
        wascolon = c == ':'
        depths = set(filter(lambda x: x >= 0, depths))
        if len(depths) == 0:
            return False
    return 0 in depths

with open("balanced_smileys.in", "r") as inp:
    for i, s in enumerate(inp.read().strip().split("\n")[1:]):
        print "Case #{}: {}".format(i+1, 'YES' if is_balanced(s) else 'NO')