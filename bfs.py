from collections import deque

def bfs_travesal(graph, pred, opaque):
    I = True
    k = set() #known
    F = deque() #unknown
    while F or I:
        if I:
            N = graph.roots()
        else: N = graph.neighbors(F.popleft())
        I = False
        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
                terminate = pred(n, opaque)
                if terminate:
                    return(opaque, k)
    return(opaque, k)

def predicate_finder(graph, predicate):
    def check_pred(n, a): # [bool, count, n]
        a[1] += 1
        a[0] = predicate(n)
        if a[0]:    
            a[2] = n
        return a[0]
    return bfs_travesal(graph, check_pred, [False, 0, None])
