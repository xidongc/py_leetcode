class Solution(object):

    def numMatchingSubseq(self, S, words):
        hashmap = dict()
        for i, s in enumerate(S):
            hashmap[s] = hashmap.get(s, list())
            hashmap[s].append(i)

        count = 0
        for word in words:
            if self.containsMatching(hashmap, word):
                count += 1
        return count

    def containsMatching(self, hashmap, word):
        startIdx = -1
        for t in word:
            if t in hashmap:
                startIdx = self.binarySearch(hashmap[t], startIdx)
                if startIdx == -1:
                    return False
            else:
                return False
        return True

    def binarySearch(self, wordlist, startIdx):
        start = 0
        end = len(wordlist) - 1

        while start < end - 1:
            mid = start + (end - start) // 2
            if wordlist[mid] > startIdx:
                end = mid
            else:
                start = mid

        if wordlist[start] > startIdx:
            return wordlist[start]
        elif wordlist[end] > startIdx:
            return wordlist[end]
        else:
            return -1
