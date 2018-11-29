import collections

# 有环的情况不能handle
class Solution(object):
    def allPathsSourceTarget(self, graph):
        des = len(graph) - 1
        # Store paths
        paths = [[0]]
        res = []
        while paths:
            curPath = paths.pop()
            for node in graph[curPath[-1]]:
                if node == des:
                    res.append(curPath + [node])
                else:
                    paths.append(curPath + [node])
        return res


s = Solution()
s.allPathsSourceTarget([[1,2],[3],[3],[]])



