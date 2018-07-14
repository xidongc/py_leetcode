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
# 用208字典树的search add startwith的func，遍历所有点，每个点dfs都做看是否在trie中。
# 因为一个点只能用一遍，所以肯定要用visited[][]啊,用完要还原
