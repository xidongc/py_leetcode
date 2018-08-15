# num = int, list(map(int,str(num))),因为map（左，iterable）
# list of int:num, int(''.join(num))
# list 随意swap，string不可以，int甚至不能index
# ''.join(list),list of string可以，list of int不行，必须用map(str,num)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return num
        num = list(map(int, str(num)))
        maxIndex = len(num) - 1
        lowIndex = len(num) - 1
        swapPair = []
        for i in range(len(num) - 2, -1, -1):
            if num[i] > num[maxIndex]:
                maxIndex = i
            elif num[i] < num[maxIndex]:
                lowIndex = i
                swapPair = [lowIndex, maxIndex]
        if swapPair:
            num[swapPair[0]], num[swapPair[1]] = num[swapPair[1]], num[swapPair[0]]
        return int(''.join(list(map(str, num))))