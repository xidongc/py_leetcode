class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_val = float("inf")
        self.min_stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_val = min(x, self.min_val)
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()
        if len(self.stack) == 0:
            self.min_val = float("inf")
        else:
            self.min_val = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
