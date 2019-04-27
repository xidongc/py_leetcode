class Solution(object):

    def removeInvalid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open, close = 0, 0
        output = list()
        for si in s:
            if si == "(":
                open += 1
            elif si == ")":
                if close >= open:
                    continue
                close += 1
            output.append(si)

        output.reverse()
        s = "".join(output)
        output = list()
        open, close = 0, 0
        for si in s:
            if si == ")":
                open += 1
            elif si == "(":
                if close >= open:
                    continue
                close += 1
            output.append(si)
        output.reverse()
        return "".join(output)
