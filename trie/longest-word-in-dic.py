class TreeNode(object):

    def __init__(self, val: str):
        if val.isalnum():
            self.val = val
            self.children = [None]*26


class Solution(object):

    def __init__(self):
        self.root = TreeNode('0')
        self.result = ""

    def longestWord(self, words):

        """
        :type words: List[str]
        :rtype: str
        """

        words = list(set(words))
        for word in words:
            word = word.lower()
            self.insert(word)
        self.find_longest_word(self.root, [], words)

        if len(self.result) <= 0:
            return None
        return self.result

    def insert(self, word):
        curr = self.root
        for w in word:
            if curr.children[ord(w) - ord('a')] is None:
                tmp = TreeNode(w)
                curr.children[ord(w) - ord('a')] = tmp
            curr = curr.children[ord(w) - ord('a')]

    def find_longest_word(self, node, curr, words):
        ret = ''.join(curr)
        if ret in "" or ret in words:
            if len(ret) > len(self.result):
                self.result = ret

        for x in node.children:
            if x is not None:
                if ret in "" or ret in words:
                    curr.append(x.val)
                    self.find_longest_word(x, curr, words)
                    curr.pop()


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
s = Solution()
print(s.longestWord(words))
