class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.put(val)
        if self.k > len(self.nums):
            return self.nums[-1]
        return self.nums[-self.k]

    def put(self, val):
        if self.nums:
            lo, hi = 0, len(self.nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if self.nums[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            self.nums.insert(lo, val)
        else:
            self.nums = [val]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)