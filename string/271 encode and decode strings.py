# 记在小本本上啦
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return res
        for str in strs:
            for c in str:
                if c == ":":
                    res += ":"
                res += c
            res += ":;"
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        string = ""
        i = 0
        while i < len(s):
            if s[i] == ':':
                i += 1
                if s[i] == ';':
                    res.append(string)
                    string = ""
                else:
                    string += s[i]
            else:
                string += s[i]
            i += 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))