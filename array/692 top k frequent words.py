import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        a = collections.Counter(words).most_common()
        a.sort(key=lambda x: (-x[1], x[0]))
        return [a[i][0] for i in range(0, k)]
