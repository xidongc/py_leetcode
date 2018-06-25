class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s:
            return res
        if len(s) == 1:
            return [s]
        map = {}
        oddStr = ""
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        for c in map.keys():
            if map[c]%2 != 0:
                oddStr += c
        if len(oddStr) > 1:return res
        
        def generate(s, temp):
            if len(temp) == len(s):
                res.append(temp)
            for i in map.keys():
                if map[i] > 1:
                    map[i] -= 2
                    generate(s, i + temp + i)
                    map[i] += 2
        generate(s,"" if len(oddStr) == 0 else oddStr)

        return res
        # Input: "aabb"
        # Output: ["abba", "baab"]
