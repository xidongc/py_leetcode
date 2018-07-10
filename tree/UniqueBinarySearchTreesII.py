# Definition for a binary tree node.

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return[]
        return self.dfs(1,n)
    def dfs(self,start,end):
        if start > end:
            return [None]
        res = []
        for i in range(start,end + 1):
            leftTree = self.dfs(start,i-1)
            rightTree = self.dfs(i+1,end)
            for j in leftTree:
                for k in rightTree:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    res.append(root)
        # print(res)
        return res
            
      Input: 3
      Output:
      [
        [1,null,3,2],
        [3,2,null,1],
        [3,1,null,null,2],
        [2,1,3],
        [1,null,2,null,3]
      ]
