class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.words = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.words[key] = val
        _end = "_end_"
        curr = self.root
        for k in key:
            curr = curr.setdefault(k, {})
        curr["_end"] = _end

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        words = self.find_prefix_words(prefix)
        cnt = 0
        for word in words:
            cnt += self.words[word]
        return cnt

    def find_prefix_words(self, prefix):
        curr = self.root
        for p in prefix:
            tmp = curr.get(p, None)
            if tmp is None:
                return []
            else:
                curr = tmp

        result = []
        self.dfs(curr, prefix, result)
        return result

    def dfs(self, curr, prefix, result):
        if "_end" in curr:
            result.append(prefix)
        if curr is {}:
            return
        for x in curr.keys():
            if x is not "_end":
                self.dfs(curr[x], prefix+str(x), result)






