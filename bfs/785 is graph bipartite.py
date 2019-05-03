class Solution(object):

    def isBipartite(self, graph) -> bool:

        # Corner case
        if len(graph) == 0:
            return True

        color = {}

        for i in range(len(graph)):
            if i not in color:
                color[i] = 1
                queue = list()
                queue.append(i)
                while len(queue) > 0:
                    curr = queue.pop(0)
                    for g in graph[curr]:
                        if g not in color:
                            color[g] = -color[curr]
                            queue.append(g)
                        else:
                            if color[g] == color[curr]:
                                return False
        return True
