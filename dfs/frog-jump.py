# 403, https://leetcode.com/problems/frog-jump/description/


# Sol-1: using DFS, LTE
# max recursive is 1000 by default, input len(stones) > 1000 will get overflow
import sys
sys.setrecursionlimit(1000000)


class Solution(object):

    def canCross(self, stones):

        """
        :type stones: List[int]
        :rtype: bool
        """

        # dfs solution, LTE
        # time complexity: O(2^n - 3^n) depending on steps

        if not stones or len(stones) == 0:
            return False

        if len(stones) >= 2 and stones[1] != 1:
            return False

        ret = False

        def helper(curr, i, step):
            nonlocal ret
            if i == stones[-1]:
                ret = True
                return True
            for j in [step-1, step, step+1]:
                if j > 0 and i+j in stones:
                    curr.append(i+j)
                    helper(curr, i+j, j)
                    curr.pop()

        curr = []
        helper(curr, 1, 1)
        return ret


# Sol-2:


s = Solution()
print(s.canCross([0,1,3,5,6,8,12,17]))

