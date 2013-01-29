import re
mem = {}
def is_balanced(s):
    try:
        return mem[s]
    except KeyError:
        def _(s):
            if re.search(r'[^a-z: ()]', s):
                return False
            # s = re.sub(r'[^():]', '', s)
            if re.match(r'^[a-z: ]*$', s):
                return True
            if s == ':)' or s == ':(':
                return True
            if s[0] == '(' and s[-1] == ')':
                if is_balanced(s[1:-1]):
                    return True
            for i in range(1,len(s)):
                a, b = s[:i], s[i:]
                if is_balanced(a) and is_balanced(b):
                    return True
            return False
        mem[s] = _(s)
        return mem[s]

with open("balanced_smileys.in", "r") as inp:
    for i, s in enumerate(inp.read().strip().split("\n")[1:]):
        print "Case #{}: {}".format(i+1, 'YES' if is_balanced(s) else 'NO')