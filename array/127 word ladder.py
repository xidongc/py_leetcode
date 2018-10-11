import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList :
            return 0
        wordSet = set(wordList)
        charString = string.ascii_lowercase
        length = 1
        wordLen = len(beginWord)
        left = set()
        left.add(beginWord)
        while left:
            if endWord in left:
                return length
            wordSet -= left
            left = wordSet & {word[:i] + letter + word[i+1:] for i in range(wordLen) for letter in charString for word in left}
            length += 1
        return 0
s = Solution()
s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])