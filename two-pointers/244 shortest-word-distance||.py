import collections
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordDict = collections.defaultdict(list)
        for i,w in enumerate(words):
            self.wordDict[w].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wList1 = self.wordDict[word1]
        wList2 = self.wordDict[word2]
        res = 2**32 - 1
        i,j = 0,0
        # 理解这里虽然是and条件， 但已经挑出所有的min可能
        while i < len(wList1) and j < len(wList2):
            res = min(res,abs(wList1[i] - wList2[j]))
            if wList1[i] <= wList2[j]:
                i += 1
            else:
                j += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)