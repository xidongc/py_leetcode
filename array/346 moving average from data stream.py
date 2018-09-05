#design
#前缀和数组
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.index = 0
        self.sumList = [0] * (size + 1)
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        def mod(index):
            return index % (self.size + 1)

        self.index += 1
        self.sumList[mod(self.index)] = self.sumList[mod(self.index - 1)] + val
        if self.index > self.size:
            return (self.sumList[mod(self.index)] - self.sumList[mod(self.index - self.size)]) / float(self.size)
        else:
            return self.sumList[self.index] / float(self.index)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)