import collections
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        if not board or not hand:
            return -1
        handMap = collections.defaultdict(int)
        for l in hand:
            handMap[l] += 1
        board += "#"
        res = self.helper(board,handMap)
        return res if res != 123456789 else -1
    def helper(self, board, handMap):
        s = self.removeConsecutive(board)
        if s == "#":
            return 0
        res = 123456789
        i, j = 0, 0
        for j in range(len(s)):
            if s[j] == s[i]:
                continue
            need = 3 - (j - i)
            if s[i] in handMap and need <= handMap[s[i]]:
                handMap[s[i]] -= need
                # 每层的zuma结果对比-
                res = min(res, need + self.helper(s[:i] + s[j:], handMap))
                handMap[s[i]] += need
            i = j
        return res
    def removeConsecutive(self,board):
        i,j = 0,0
        for j in range(len(board)):
            if board[j] == board[i]:
                continue
            # 如果有重复，那就return直接退出for，没有的话就return board
            if j - i >= 3:
                return self.removeConsecutive(board[:i] + board[j:])
            i = j
        return board

s = Solution()
print(s.findMinStep("WWRRBBWW","WRBRW"))






