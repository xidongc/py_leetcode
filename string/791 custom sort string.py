# Sth similar
# 给两个string: (order, input_string), 算input_string 是否根据 order 是 sorted的。
# 具体例子:
# ('abc', 'abc') => True 来源一亩.三分地论坛.
# ('abc', 'bac') => False
# ('abc', 'qaqbqc') => True. Waral 博客有更多文章,
# ('abc', 'qcqaqb') => False
# 做法:
# 存一个order的哈希表 char_to_idx
# loop through input_string, 如果某个character 在char_to_idx中存在, append到一个list中
# 最后看这个list是否是non-decreasing的就ok。（其实不用list，直接看是否non-decreasing就行）
# Hashmap??
import collections
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        countDict = dict(collections.Counter(T))
        res = ''
        for s in S:
            if s in countDict:
                res += s * countDict[s]
                del(countDict[s])
        if countDict:
            for key in countDict:
                res += key * countDict[key]
        return res
s = Solution()
print(s.customSortString('cba','abcd'))



# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.