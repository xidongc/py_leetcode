# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = list()
        for n in nestedList[::-1]:
            self.stack.append(n)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            if self.stack[-1].isInteger():
                return True
            else:
                curr = self.stack.pop()
                for c in curr.getList()[::-1]:
                    self.stack.append(c)
        return False
