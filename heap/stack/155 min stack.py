class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        stack = []
        self.stack = stack
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()