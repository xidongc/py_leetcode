class Solution(object):

    def removeInvalidParentheses(self, s: str):

        if len(s) == 0:
            return [s]

        def isValid(s):
            count = 0
            for si in s:
                if si is "(":
                    count += 1
                elif si is ")":
                    count -= 1
                if count < 0:
                    return False
            if count != 0:
                return False
            return True

        def getredundant(s):
            l = 0
            r = 0
            count = 0
            for si in s:
                if si is "(":
                    count += 1
                elif si is ")":
                    if count > 0:
                        count -= 1
                    elif count == 0:
                        r += 1
            l += count
            return l, r

        def dfs(s, start, l, r, ret):

            if l == 0 and r == 0:
                if isValid(s):
                    if s not in ret:
                        ret.append(s)
                return

            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    # remove duplicate calculation eg: "(((" or ")))
                    pass
                elif r > 0 and s[i] is ")":
                    news = s[0:i] + s[i + 1:]
                    dfs(news, i, l, r - 1, ret)

                elif r == 0 and l > 0 and s[i] is "(":
                    news = s[0:i] + s[i + 1:]
                    dfs(news, i, l - 1, r, ret)

        l, r = getredundant(s)
        ret = list()
        dfs(s, 0, l, r, ret)
        if len(ret) == 0:
            ret.append("")
        return ret
