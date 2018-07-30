# import collections
# def findItinerary(tickets):
#     targets = collections.defaultdict(list)
#     for a, b in sorted(tickets)[::-1]:
#         targets[a] += b,
#     route = []
#     def visit(airport):
#         while targets[airport]:
#             visit(targets[airport].pop())
#         route.append(airport)
#     visit('J')
#     return route[::-1]
# findItinerary([["J","A"],["J","D"],["A","C"],["B","C"],["C","D"],["C","J"],["D","A"],["D","B"]])
print([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print(sorted([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]))
print(sorted([823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))


