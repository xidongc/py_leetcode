# – 单词在字典中出现次数等于对应缩写在字典中出现次数 -> unique
# – 单词在字典中出现次数不等于对应缩写在字典中出现次数 -> not unique
import collections
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict = dictionary
        self.abbvDict = collections.defaultdict(int)
        self.wordDict = collections.defaultdict(int)
        for string in self.dict:
            self.abbvDict[self.abbv(string)] += 1
            self.wordDict[string] += 1
    # isunique被多次调用
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.abbvDict[self.abbv(word)] == self.wordDict[word]

    def abbv(self,string):
        return string if len(string) <= 2 else string[0] + str(len(string) - 2) + string[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
dictionary = ["dog"]
obj = ValidWordAbbr(dictionary)
# print(obj.isUnique("dear"))
print(obj.isUnique("dog"))