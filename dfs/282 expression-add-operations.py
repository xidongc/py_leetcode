class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def helper(num):
            # 去重！！！！
            curList = [num] if str(int(num)) == num else []
            for i in range(len(num)-1):
                left = helper(num[:i + 1])
                right = helper(num[i + 1:])
                curList += [leftPart + '+' + rightPart for leftPart in left for rightPart in right]
                curList += [leftPart + '-' + rightPart for leftPart in left for rightPart in right]
                curList += [leftPart + '*' + rightPart for leftPart in left for rightPart in right]
            return set(curList)

        allList = helper(num)
        for item in allList:
            if eval(item) == target:
                res.append(item)
        return res
s = Solution()
print(s.addOperators('105',5))
