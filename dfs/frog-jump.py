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
# memorize for those dead end, Accepted
# get sol from https://leetcode.com/problems/frog-jump/discuss/88873/Python-DFS-easy-understanding-using-memo
# don' t expect myself to write it, can skip it when review
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        target, stones, memo = stones[-1], set(stones), set()
        return self.backtrack(stones, 1, 1, target, memo)

    def backtrack(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if jump <= 0 or pos not in stones:
            return False
        for j in (jump-1, jump, jump+1):
            if self.backtrack(stones, pos+j, j, target, memo):
                return True
        memo.add((pos, jump))   # record bad position and jump
        return False


# test
s = Solution()
print(s.canCross([0,1,3,5,6,8,12,17]))

