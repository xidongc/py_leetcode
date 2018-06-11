class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if not flowerbed:
            return False
        count = 1
        res = 0
        for num in flowerbed:
            if num == 0:
                count += 1
            elif count:
                res += (count-1) // 2
                count = 0
        if count:
            res += count // 2
        return res >= n
        
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
