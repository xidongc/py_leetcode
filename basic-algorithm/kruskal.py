class Edge:
    def __init__(self, cost=0., u='', v=''):
        self.cost = cost
        self.u = u
        self.v = v


def get_vextex_and_edge(n, m):
    vextex = ['' for i in range(n)]
    edge = [Edge() for i in range(m)]
    return vextex, edge


def kruskal(vextex: list, edge: list):
    vset = []

    def cmp(a, b):
        return a.cost - b.cost

    edge.sort(key=lambda x: x.cost)
    for e in edge:
        u, v = vextex.count(e.u), vextex.count(e.v)
        if u and v: continue
        if u: vset.append(u)
        if v: vset.append(v)
        if len(vset) == len(vextex):
            break
    return edge
# 输入
# 点集合vextex， 边集合edge
#
# 算法步骤
# 将所有边按代价值从小到大排序，并初始化一个空点集A以及一个空边集B。
# 依次遍历所有边，若当前边中存在一个点不属于A，那么则将该边加入B，并将边的两点加入A；若当前边的两点都已加入A中，则跳过该边。
# 按2的做法，直到A=vextex结束。
# 用bfs点来判断点的个数是否能连成mst，
