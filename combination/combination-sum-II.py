# cxd
class Solution(object):

    def __init__(self):
        self.ret = []

    def combinationSum2(self, candidates, target):

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) < 1:
            return self.ret

        curr = []
        candidates.sort()
        self.dfs(candidates, target, curr)
        self.remove_dup()
        return self.ret

    def dfs(self, candidates, target, curr):
        if target == 0:
            self.ret.append(curr[:])
            return

        elif target > 0:
            for i, candidate in enumerate(candidates):
                curr.append(candidate)
                self.dfs(candidates[(i+1):],
                         target-candidate, curr)
                curr.pop()

        else:
            return

    def remove_dup(self):
        for x in self.ret:
            while self.ret.count(x) > 1:
                self.ret.remove(x)
#lmf
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.helper(candidates, target, [], res, 0)
        return res

    def helper(self, candidates, target, curr, res, start):

        if target == 0:
            res.append(curr[:])
            return
        for i in range(start, len(candidates)):
# skip from the second same number since all the situations with this num is in the res.
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break
            self.helper(candidates, target - candidates[i], curr + [candidates[i]], res, i + 1)
s = Solution()
candidates = [29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5]
target = 28
print(s.combinationSum2(candidates, target))











