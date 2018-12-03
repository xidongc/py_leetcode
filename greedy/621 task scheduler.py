# 先统计词频，再排序，从后往前找到第一个不是最大词频的下标i
# 结果是tasks.length或(c[25] - 1) * (n + 1) + 25 – i中大的那一个，
# 25-i就是最大词频的任务类，
# 证明：最大词频是k，则创建k个块，每一块开头是最大词频的任务构成的(输入AACCCDDEEE，
# 则开头是CE)，词频由大到小插入每一块。97.69%，10ms
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cList = [0]*26
        for l in tasks:
            cList[ord(l)-ord('A')] += 1
        cList.sort()
        i = 25
        while i >= 0 and cList[i] == cList[25]:
            i -= 1
        #     25 - i is the max freq letter count
        return max(len(tasks),(cList[25]-1)*(n+1)+25-i)

# AAAABBBEEFFGG 3
#
# A出现了4次，最多，mx=4，那么可以分为mx-1=3块，如下：
#
# A---A---A---
#
# 每块有n+1=4个，最后还要加上末尾的一个A，也就是25-24=1个任务，最终结果为13：
# (cList[25]-1)*(n+1)+25-i is the maximum frame size, if it would not fit
# task length can fit though
s = Solution()
s.leastInterval('AACCCBEEE',2)