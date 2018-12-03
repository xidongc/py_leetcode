class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        _end = "_end_"
        current_dict = self.root
        for w in word:
            current_dict = current_dict.setdefault(w, {})
        current_dict["_end"] = _end

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        _end = "_end_"
        curr = self.root
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                return False
        return curr.setdefault("_end", None) == _end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        _end = "_end_"
        curr = self.root
        for w in prefix:
            if w in curr:
                curr = curr[w]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)