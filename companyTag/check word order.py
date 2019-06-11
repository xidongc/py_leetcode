class Word(str):

    def __lt__(self, other):
        for i in range(min(len(other), len(self))):
            if other[i] > self[i]:
                return True
            elif other[i] < self[i]:
                return False

        if len(self) < len(other):
            return True
        return False


class Solution(object):

    def checkWordOrder(self, words):

        words = [Word(word) for word in words]
        words.sort()
        print(words)

s = Solution()
ret = s.checkWordOrder(['a', 'aa', 'cb', 'bc', "aaa"])
print(ret)
