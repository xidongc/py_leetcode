class Solution(object):

    def minWindow(self, s: str, t: str) -> str:

        match, curr = {}, {}
        for ti in t:
            if ti not in match:
                match[ti] = 1
            else:
                match[ti] = match[ti] + 1
            curr[ti] = 0

        j = 0
        hashset = set()
        result, result_len = s, float("inf")

        for i in range(len(s)):
            while j < len(s):
                if len(hashset) < len(curr):
                    if s[j] in curr:
                        curr[s[j]] += 1
                        if curr[s[j]] >= match[s[j]]:
                            hashset.add(s[j])
                    j += 1
                else:
                    break
            if j - i < result_len and len(hashset) >= len(curr):
                result = s[i: j]
                result_len = j - i
            if s[i] in curr:
                curr[s[i]] -= 1
                if curr[s[i]] < match[s[i]] and s[i] in hashset:
                    hashset.remove(s[i])
        return result if result_len != float("inf") else ""
