class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - 1
        count = 0
        while left < right:
            if abs(arr[left]-x) > abs(arr[right]-x):
                left = left + 1
            else:
                right = right - 1
            count += 1
            if count == len(arr) - k:
                break

        return arr[left:right+1]