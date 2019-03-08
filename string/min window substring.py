from collections import Counter


class Solution(object):

    def minWindow(self, s: str, t: str) -> str:

        j = 0
        target = Counter(t)
        window = dict()
        size = len(target)
        current = 0
        ret = s
        set_or_not = False

        for i in range(len(s)):
            while j < len(s):
                if j < len(s) and current < size:
                    if s[j] in target:
                        window[s[j]] = window.get(s[j], 0) + 1
                        if window[s[j]] == target[s[j]]:
                            current += 1
                    j += 1
                else:
                    break

            if current == size:
                if j - i <= len(ret):
                    ret = s[i:j]
                    set_or_not = True

            if s[i] in target:
                window[s[i]] = window.get(s[i], 1) - 1

                if window[s[i]] < target[s[i]]:
                    current -= 1

                if window[s[i]] == 0:
                    window.pop(s[i])

        if set_or_not:
            return ret
        else:
            return ""