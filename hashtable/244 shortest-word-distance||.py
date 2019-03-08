class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordList = words

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return 0
        map = {word1 : -1, word2 : -1}
        dis = len(self.wordList)
        for i in range(len(self.wordList)):
            if self.wordList[i] == word1:
                dis = min(abs(map[word2] - map[word1]), abs(map[word2] - i))
                map[word1] = i
            elif self.wordList[i] == word2:
                dis = min(abs(map[word2] - map[word1]), abs(map[word1] - i))
                map[word2] = i
        return dis

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)