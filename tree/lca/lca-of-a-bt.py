class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        leftArray = self.findAncestorList(root, p)
        rightArray = self.findAncestorList(root, q)
        self.printAncestorList(leftArray);
        self.printAncestorList(rightArray);

        for p in leftArray[::-1]:
            if p in rightArray:
                return p

        return None

    def findAncestorList(self, root, eleRoot):
        ancestorList = list()
        def dfs(root, eleRoot, curr):
            nonlocal ancestorList
            if root is eleRoot:
                ancestorList = curr[:]
                print(ancestorList)
            for i in [root.left, root.right]:
                if i is not None:
                    curr.append(i)
                    dfs(i, eleRoot, curr)
                    curr.pop()
        dfs(root, eleRoot, [root])
        # print(ancestorList)
        return ancestorList

    def printAncestorList(self, ancestorList):
        for node in ancestorList:
            print(node.val)