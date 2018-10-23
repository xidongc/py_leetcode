from queue import PriorityQueue


class Edges(object):

    def __init__(self, from_node, to_node, val):
        self.from_node = from_node
        self.to_node = to_node
        self.val = val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val


class Graph(object):

    def __init__(self, vertexs: list, edges: list):
        # e: (1,2,0.1)  1->2 w=0.1 wuxiang
        self.V = len(vertexs)
        self.E = len(edges)
        self.vertexs = vertexs
        self.adj = dict()
        self.visited = dict()
        for v in vertexs:
            self.adj[v] = list()
            self.visited[v] = False
        for e in edges:
            self.adj[e[0]].append(Edges(e[0], e[1], e[2]))
            self.adj[e[1]].append(Edges(e[1], e[0], e[2]))

    def get_neighbors(self, curr: Edges):
        # not finished return neighbor's node
        node = curr.to_node
        return self.adj[node]

    def all_node_visited(self):
        for k, v in self.visited.items():
            if v is False:
                return False
        return True

    def MST(self, node, method="prime"):
        if method is "prime":
            ret = list()
            # using prime alg
            pq = PriorityQueue()
            pq.put(Edges(node, node, 0))
            while not pq.empty():
                curr = pq.get()
                if self.visited[curr.to_node] is False:
                    self.visited[curr.to_node] = True
                    if curr.val != 0:
                        ret.append((curr.from_node, curr.to_node, curr.val))
                    adj_vertexs = self.get_neighbors(curr)
                    for v in adj_vertexs:
                        if self.visited[v.to_node] is False:
                            pq.put(v)

                if self.all_node_visited():
                    break
            print(ret)
            return ret
        elif method is "kruskal":
            pass
        else:
            return None

vertexs = [x for x in range(8)]
# sample using p402 graph
edges = [(0,7,0.16), (2,3,0.17), (1,7,0.19),
         (0,2,0.26), (5,7,0.28), (1,3,0.29),
         (1,5,0.32), (2,7,0.34), (4,5,0.35),
         (1,2,0.36), (4,7,0.37), (0,4,0.38),
         (6,2,0.4), (3,6,0.52), (6,0,0.58),
         (6,4,0.93)]
g = Graph(vertexs, edges)
g.MST(0)



