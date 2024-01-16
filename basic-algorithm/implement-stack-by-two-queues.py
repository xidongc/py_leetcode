import collections


class Stack:
    """
    @constructor
    """
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # 每次入队都加入queue1
        self.queue1.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # 如果queue1为空，代表栈顶在queue2，交换
        if not self.queue1:
            self.queue1, self.queue2 = self.queue2, self.queue1
        # 将queue1前n-1个放入queue2，弹出最后的元素
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        self.queue1.popleft()
    """
    @return: An integer
    """
    def top(self):
        # 如果queue1为空，代表栈顶在queue2，交换
        if not self.queue1:
            self.queue1, self.queue2 = self.queue2, self.queue1
        # 将queue1前n-1个放入queue2，获得最后的元素
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        return self.queue1[0]
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # 如果两个队列都空，代表栈是空的
        return not self.queue1 and not self.queue2
