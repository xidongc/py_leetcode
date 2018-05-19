class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate(start, stop):
            vs = []
            if start > stop:
                return [None]
            elif start == stop:
                return [TreeNode(start)]

            for i in range(start, stop+1):
                l = generate(start, i-1)
                r = generate(i+1, stop)

                for j in range(len(l)):
                    for k in range(len(r)):
                        t = TreeNode(i)
                        t.left = l[j]
                        t.right = r[k]
                        vs.append(t)
            return vs
        if n == 0:
            return []
        return generate(1, n)

n = 3
s = Solution()
print(s.generateTrees(n))
