class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        pos = 0
        count = 0
        res = ''
        countList = []
        strList = []
        while pos < len(s):
            if s[pos].isdigit():
                while s[pos].isdigit():
                    count = 10 * count + int(s[pos])
                    pos += 1
                countList.append(count)
                count = 0
                pos -= 1
            elif s[pos] == '[':
                strList.append(res)
                res = ''
            elif s[pos] == ']':
                times = countList.pop()
                temp = strList.pop()
                for i in range(times):
                    temp += res
                res = temp
            else:
                res += s[pos]
            pos += 1
        return res
                #用stack啊啊啊啊
