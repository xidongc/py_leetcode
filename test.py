class Solution(object):
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dic = dict()
        for word in words:
            dic[word] = dic.get(word, 0) + 1

        dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
        print(dic[0:k])

s = Solution()
print(s.topKFrequent(["a","b","c"], 2))


