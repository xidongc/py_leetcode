class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n != len(edges) + 1:
            return False
        nums = [-1 for i in range(n)]
        for edge in edges:
            x = self.find(nums, edge[0])
            y = self.find(nums, edge[1])
            if x == y:
                return False
            nums[x] = y
        return True
    def find(self, nums, num):
        if nums[num] == -1:
            return num
        return self.find(nums, nums[num])
#Union find Algorithm, find if two node has the same root node. If so, there would be a circle in within the edges.
#Edge Case: s.validTree(1,[]) 不能一上来就做这个not edge的判断啊 
