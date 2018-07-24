# sliding window
# 有非words直接把left拉去j + wl， words数量不匹配也是挪left，right boundary j+wl不动

# dict.clear()
# In addition, sometimes the dict instance might be a subclass of dict (defaultdict for example).
# In that case, using clear is preferred,
import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        countDict = collections.defaultdict(int)
        curDict = collections.defaultdict(int)
        res = []
        for word in words:
            countDict[word] += 1
        wordLen = len(words[0])
        for i in range(0,wordLen):
            left = i
            count = 0
            curDict.clear()
            for j in range(i,len(s) - wordLen + 1, wordLen):
                str = s[j:j+wordLen]
                if str in words:
                    curDict[str] += 1
                    if curDict[str] <= countDict[str]:
                        count += 1
                    else:
                        while curDict[str] > countDict[str]:
                            curStr = s[left:left+wordLen]
                            curDict[curStr] -= 1
                            if curDict[curStr] < countDict[curStr]:
                                count -= 1
                            left += wordLen
                    if count == len(words):
                        res.append(left)
                        curStr = s[left:left+ wordLen]
                        curDict[curStr] -= 1
                        count -= 1
                        left += wordLen

                else:
                    curDict.clear()
                    count = 0
                    left = j + wordLen
        return res

#
# s = Solution()
#
#
# s.findSubstring("aaaaaaaa", ["aa","aa","aa"])

# "wordgoodgoodgoodbestword"
# ["word","good","best","good"]

# "barfoofoobarthefoobarman"
# ["bar","foo","the"]