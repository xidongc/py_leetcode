class Solution(object):

    def __init__(self):
        self.root = dict()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        matches = list()
        if len(words) == 0:
            return matches
        elif len(board) == 0 or not board:
            return matches

        self.build_trie(words)
        print(self.root)

        h = len(board)
        w = len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in self.root.keys():
                    curr = self.root[board[i][j]]
                    mark_list = [(i, j)]
                    self.dfs(i, j, board, matches, curr, h, w, board[i][j], mark_list)

        matches = list(set(matches))
        matches.sort()
        print(matches)
        return matches

    def build_trie(self, words):
        _end = "_end_"
        for word in words:
            curr = self.root
            for w in word:
                curr = curr.setdefault(w, {})
            curr["_end"] = _end

    def dfs(self, i, j, board, matches, curr, h, w, prefix, mark_list):

        if "_end" in curr:
            matches.append(prefix)
        if curr is {}:
            return

        if i > 0 and board[i-1][j] in curr.keys() and (i-1, j) not in mark_list:
            mark_list.append((i-1, j))
            self.dfs(i-1, j, board, matches, curr[board[i-1][j]], h, w, prefix+board[i-1][j], mark_list)
            mark_list.pop()
        if i < h-1 and board[i+1][j] in curr.keys() and (i+1, j) not in mark_list:
            mark_list.append((i+1, j))
            self.dfs(i+1, j, board, matches, curr[board[i+1][j]], h, w, prefix+board[i+1][j], mark_list)
            mark_list.pop()
        if j > 0 and board[i][j-1] in curr.keys() and (i, j-1) not in mark_list:
            mark_list.append((i, j-1))
            self.dfs(i, j-1, board, matches, curr[board[i][j-1]], h, w, prefix+board[i][j-1], mark_list)
            mark_list.pop()
        if j < w-1 and board[i][j+1] in curr.keys() and (i, j+1) not in mark_list:
            mark_list.append((i, j+1))
            self.dfs(i, j+1, board,  matches, curr[board[i][j+1]], h, w, prefix+board[i][j+1], mark_list)
            mark_list.pop()


s = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
s.findWords(board, words)