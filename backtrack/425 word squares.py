import collections
class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return [[]]
        square = []
        prefixMap = collections.defaultdict(list)
        for word in words:
            # ''的情况要考虑
            prefix = ''
            prefixMap[prefix].append(word)
            for c in word:
                prefix += c
                prefixMap[prefix].append(word)
        def dfs(words, pos, tmpList):
            prefix = ''
            if pos < len(words[0]) and tmpList:
                for i in range(pos):
                    prefix += tmpList[i][pos]
                if prefix not in prefixMap:
                    return
            if pos == len(words[0]):
                square.append(tmpList[:])
                return
            for word in prefixMap[prefix]:
                dfs(words,pos+1,tmpList+[word])
                    # print(square)
        dfs(words,0,[])
        return square
s = Solution()
# 可以重复使用word
# 浅拷贝tmpList[:]
# 跳出情况的层数？
# square.append放在for里面会重复append，位置
print(s.wordSquares(["abat","baba","atan","atal"]))