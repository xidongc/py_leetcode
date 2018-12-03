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
        # 按字母顺序从小到大排序
        tickets.sort(key=lambda ticket: (ticket[0],ticket[1]))
        for ticket in tickets:
            airMap[ticket[0]].append(ticket[1])
        def visit(airport):
            while airMap[airport]:
                # 先pop权重大的，这样倒序之后字典序就小了？？
                visit(airMap[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
# 字典序，第一个字母相同就去找第二个字母排序
s = Solution()
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])