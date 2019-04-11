# class MedianFinder(object):
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.orderedList = []
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         if not self.orderedList:
#             self.orderedList.append(num)
#         else:
#             low, high = 0, len(self.orderedList)
#             while low < high:
#                 mid = (low + high) // 2
#                 if num < self.orderedList[mid] :
#                     high = mid
#                 else:
#                     low = mid + 1
#             self.orderedList = self.orderedList[:low] + [num] + self.orderedList[low:]
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if self.orderedList:
#             pos = len(self.orderedList) // 2
#             return self.orderedList[pos] if len(self.orderedList) % 2 == 1 else (self.orderedList[pos] +
#                                                                                  self.orderedList[pos - 1]) / 2
#         else:
#             return -1
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap
    # 大小堆，大堆存正数，较大的一摞，小堆存负数，较小的一摞

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        print("small", self.small)
        print("large", self.large)
    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
# Your MedianFinder object will be instantiated and called as such:
# memory有限怎么办(heap一次把所有的data都放进memory,
# 如果不够的话可以比如存number的count/  that's 2^32 buckets,
# or at most 2^33 integers (key and count for each int),
# which is 2^35 bytes or 32GB. Then at any point, to find the median,
# just use the counts to determine which integer is the middle element.
# This takes constant time (albeit a large constant, but constant nonetheless
obj = MedianFinder()
obj.addNum(7)
obj.addNum(2)
# print(obj.findMedian())
obj.addNum(3)
obj.addNum(1)
obj.addNum(8)
print(obj.findMedian())