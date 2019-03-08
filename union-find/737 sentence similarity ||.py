import collections
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if words1 == words2:
            return True
        elif len(words1) != len(words2) or pairs == []:
            return False
        else:
            parent = dict()
            for pair in pairs:
                parent[pair[0]] = pair[0]
                parent[pair[1]] = pair[1]
            for pair in pairs:
                p0,p1 = pair[0],pair[1]
                while parent[p0] != p0:
                    p0 = parent[p0]
                while parent[p1] != p1:
                    p1 = parent[p1]
                parent[p0] = p1
            for i in range(len(words1)):
                w1,w2 = words1[i],words2[i]
                # 一种是word相同的特殊情况
                if w1 == w2:
                    continue
                # 一种是word不在pair里面的情况
                if w1 not in parent or w2 not in parent:
                    return False
                while w1 != parent[w1]:
                    w1 = parent[w1]
                while w2 != parent[w2]:
                    w2 = parent[w2]
                if w1 != w2:
                    return False
        return Truereverse