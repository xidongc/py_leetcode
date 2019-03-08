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

#lmf
class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        # Whether this node is the end of this word
        self.formWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        curNode.formWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return curNode.formWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for char in prefix:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return True


class Solution:

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trieDict = Trie()
        res = []
        if not board or not board[0]:
            return []
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for word in words:
            trieDict.insert(word)
        def dfs(board, visited, i, j, curStr):
            print("i",i)
            print("j",j)
            print(visited)
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
                return
            curStr += board[i][j]
            if not trieDict.startsWith(curStr):
                return
            if trieDict.search(curStr) and curStr not in res:
                # 上述if对于重复words的情况。。。。
                res.append(curStr)
            visited[i][j] = True
            dfs(board, visited, i + 1, j,curStr)
            dfs(board, visited, i - 1, j,curStr)
            dfs(board, visited, i, j + 1,curStr)
            dfs(board, visited, i, j - 1,curStr)
            visited[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, visited, i, j, "")
        return res

s = Solution()
s.findWords([["a","a"]],["a"])
#
# 用208字典树的search add startwith的func，遍历所有点，每个点dfs都做看是否在trie中。
# 对于两个单词，共用一个char是没有问题的

