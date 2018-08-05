class NumArray:
    '''
    Binary indexed tree
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums) + 1
        self.nums = [0 for i in range(self.n)]
        self.arr = [0 for i in range(self.n)]
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += 1
        p = val - self.nums[i]
        self.nums[i] = val
        while i < self.n:
            self.arr[i] += p
            i += i & (-i)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(j+1) - self.query(i)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= i & (-i)
        return ret

