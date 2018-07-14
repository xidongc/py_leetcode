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
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)