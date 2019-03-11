import collections


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word and word not in self.dict[len(word)]:
            self.dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.dict[len(word)]
        for w in self.dict[len(word)]:
            for i, c in enumerate(word):
                if c != '.' and w[i] != c:
                    break
            #         进入else说明上面流程走完一遍了， 已经出现符合要求的了
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
