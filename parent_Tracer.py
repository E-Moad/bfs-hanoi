def __init__():
    self.parents = dict()

def roots():
    rs = self.operand.roots()
    for r in rs:
        parents[r] = []
    return rs

def neighbors(self, v):
    ns = self.operand.neighbors(v)
    for n in ns:
        if not parents[n]:
            parents[n] = [v]
    return ns 