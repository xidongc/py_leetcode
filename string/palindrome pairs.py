class Solution(object):

    def palindromePairs(self, words):

        pairs = list()

        # corner case
        if len(words) == 0:
            return pairs

        hashmap = dict()
        for i, word in enumerate(words):
            word = list(word)
            word.reverse()
            hashmap["".join(word)] = i

        # so far we have reverse word in dic
        for k, word in enumerate(words):
            for i in range(len(word)+1):
                if word[:i] in hashmap and hashmap[word[:i]] != k and self.isPalind(word[i:]):
                    pairs.append((k, hashmap[word[:i]]))
                if word[i:] in hashmap and hashmap[word[i:]] != k and self.isPalind(word[:i]):
                    pairs.append((hashmap[word[i:]], k))

        return list(set(pairs))

    def isPalind(self, s):
        if len(s) == 0:
            return True
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


s = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
pairs = s.palindromePairs(words)
print(pairs)