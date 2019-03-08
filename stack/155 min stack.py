# 每个元素push进来的时候存当前min进去，
# 记录当前状态
# 这方法真聪明

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: 'int') -> 'None':
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.s.append((x, curMin))

    def pop(self) -> 'None':
        self.s.pop()

    def top(self) -> 'int':
        return self.s[-1][0]

    def getMin(self) -> 'int':
        if not self.s:
            return None
        else:
            return self.s[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()