class Solution(object):

    def reverseWords(self, s: str) -> str:
        s = [x for x in s.split(" ") if len(x) > 0]
        print(s)
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return " ".join(s) if len(s) > 0 else ""
