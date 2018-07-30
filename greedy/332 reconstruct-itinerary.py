# Eulerian path.
# The nodes which have odd degrees (int and out) are the entrance or exit.
# In your example it's JFK and A.The nodes which have odd degrees (int and out) are the entrance or exit.
# If there are no nodes have odd degrees, we could follow any path without stuck until hit the last exit node
# The reason we got stuck is because that we hit the exit
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++?page=5

# print(sorted([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# [['ATL', 'JFK'], ['ATL', 'SFO'], ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'ATL']]
# print(sorted([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])[::-1])
# [['SFO', 'ATL'], ['JFK', 'SFO'], ['JFK', 'ATL'], ['ATL', 'SFO'], ['ATL', 'JFK']]
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        route = []
        airMap = collections.defaultdict(list)
        for ticket in sorted(tickets)[::-1]:
            airMap[ticket[0]].append(ticket[1])
        def visit(airport):
            while airMap[airport]:
                visit(airMap[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

