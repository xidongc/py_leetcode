import sys
import collections
# Prints to standard output.
def findLongestCycle(lines):
    # IMPLEMENTATION GOES HERE
    stack = []
    visited = {}
    res = []
    parentDict = collections.defaultdict(list)

    def dfs(visited, parentDict, stack, node):
        visited[node] = True
        stack.append(node)
        if node in parentDict:
            for parent in parentDict[node]:
                if parent not in stack:
                    if not visited[parent]:
                        dfs(visited, parentDict, stack, parent)
                else:
                    pos = stack.index(parent)
                    res.append(' '.join(sorted(stack[pos:])))
                    return
        stack.pop()

    for line in lines:
        if ':' in line:
            child, parent = line[1:-1].split(':')
            parentDict[child].append(parent)
            if child not in visited:
                visited[child] = False
            if parent not in visited:
                visited[parent] = False
    for node in visited.keys():
        if not visited[node]:
            dfs(visited, parentDict, stack, node)
    if res:
        print(res[0])
    else:
        print('None')

import networkx as nx
def findLongestCycle(lines):
    nodeSet = set()
    nodePair = []
    for line in lines:
        if ':' in line:
            child, parent = line[1:-1].split(':')
            nodeSet.add(child)
            nodeSet.add(parent)
            nodePair.append((child, parent))
# Create Directed Graph
    G=nx.DiGraph()

# Add a list of nodes:
    G.add_nodes_from(nodeSet)
# Add a list of edges:
    G.add_edges_from(nodePair)
#Return a list of cycles described as a list o nodes
    all_cycles = list(nx.simple_cycles(G))
    res = []
#Find longest cycle
    longestCycleLen = 0
    for cycle in all_cycles:
        if len(cycle) > longestCycleLen:
            longestCycleLen = len(cycle)
            res = cycle
    if not res:
        print('None')
    else:
        print(' '.join(res))
