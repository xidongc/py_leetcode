from collections import Counter


class Solution(object):

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # corner case
        if len(strs) == 0:
            return list()

        hashmap = dict()
        for i, s in enumerate(strs):
            tmp = ''.join(sorted(s))
            if tmp not in hashmap:
                hashmap[tmp] = [s]
            else:
                hashmap[tmp].append(s)

        return [hashmap[t] for t in hashmap]

# Sol-2:

class Solution(object):

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # corner case
        if len(strs) == 0:
            return list()

        counter = dict()
        hashmap = dict()

        for s in strs:
            if Counter(s) not in counter.values():
                counter[s] = Counter(s)
                hashmap[s] = [s]
            else:
                for k in counter:
                    if Counter(s) == counter[k]:
                        hashmap[k].append(s)
                        break

        return [hashmap[t] for t in hashmap]
