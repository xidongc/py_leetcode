# Complete the tasks function below.
import collections
def tasks(n, a, b):
    stack = []
    visited = [False] * (n+1)
    graph = collections.defaultdict(list)
    for i in range(len(a)):
        graph[b[i]].append(a[i])
    global circleList
    circleList = []
    def dfs(node, graph, visited, stack):
        visited[node] = True
        stack.append(node)
        if node in graph:
            for n in graph[node]:
                if n not in stack and not visited[n]:
                    dfs(n, graph, visited, stack)
                elif n in stack :
                    index = stack.index(n)
                    # stack = stack[index + 1:]
                    global circleList
                    for num in stack[index:]:
                        if num not in circleList:
                            circleList.append(num)
        stack.pop(-1)
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i, graph, visited, stack)
    return n if not circleList else n - len(circleList) + 1

print(tasks(7,[1,2,3,4,6,5],[7,6,4,1,2,1]))
# print(tasks(2,[1,2],[2,1]))