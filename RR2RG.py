class RR2RG():
    def __init__(self, operand: RootedRelation):
        self.operand = operand

    def roots(self):
        return self.operand.initial()

    def neighbors(self, c):
        actionsList = self.operand.actions(c)
        ns = []
        for a in actionsList:
            ns += [self.operand.execute(a, c)]
        return ns