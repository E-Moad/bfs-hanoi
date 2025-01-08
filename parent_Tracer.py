class ParentTracer:
    def __init__(self, operand):
        self.operand = operand
        self.parents = dict()

    def roots(self):
        rs = self.operand.roots()
        for r in rs:
            self.parents[r] = []
        return rs

    def neighbors(self, v):
        ns = self.operand.neighbors(v)
        for n in ns:
            if n not in self.parents:
                self.parents[n] = [v]
            else:
                self.parents[n].append(v)
        return ns 