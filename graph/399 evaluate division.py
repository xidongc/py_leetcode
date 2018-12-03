# zip将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[flnoat]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        map = collections.defaultdict(dict)
        for (num1,num2), val in zip(equations,values):
            map[num1][num1] = map[num2][num2] = 1.0
            map[num1][num2] = val
            map[num2][num1] = 1.0 / val
        for l1 in map:
            for l2 in map[l1]:
                for l3 in map[l1]:
                        map[l2][l3] = map[l1][l3] * map[l2][l1]
        # map.get(key,defaultval)
        return [map[num1].get(num2,-1.0) for num1,num2 in queries]
#                 float问题/别的复杂度的问题



