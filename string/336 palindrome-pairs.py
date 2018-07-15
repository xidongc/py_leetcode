class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wordDict = {y: x for x, y in enumerate(words)}
        res = set()
        def isPalindrome(word):
            length = len(word)
            for i in range(length // 2):
                if word[i] != word[length - i - 1]:
                    return False
            return True
        # 1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案
        for word in wordDict:
            if "" in wordDict and isPalindrome(word) and word != "":
                res.add((wordDict[word],wordDict[""]))
                res.add((wordDict[""],wordDict[word]))

        # 2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案
            reWord = word[::-1]
            if reWord in wordDict and wordDict[reWord] != wordDict[word]:
                res.add((wordDict[reWord],wordDict[word]))
                res.add((wordDict[word],wordDict[reWord]))

        # 3). 将当前单词word拆分为左右两半left，right。
#      3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
#      3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
#             "sbsls" "bs"; "bsbla" "al"
            for i in range(len(word)):
                left, right = word[:i], word[i:]
                reLeft,reRight = left[::-1],right[::-1]
                # for case like "s", would be split as 's' and '', but there is no '' here
                if isPalindrome(left) and reRight in wordDict and wordDict[reRight] != wordDict[word]:
                    res.add((wordDict[reRight],wordDict[word]))
                if isPalindrome(right) and reLeft in wordDict and wordDict[word] != wordDict[reLeft]:
                    res.add((wordDict[word], wordDict[reLeft]))

        #用set去重
        # set 不能存可变对象故这里只存tuple
        return list(res)
s = Solution()
print(s.palindromePairs(["s"]))

#
