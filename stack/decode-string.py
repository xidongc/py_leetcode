class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # using stack
        # time complexity:
        # seperate s first store in s

        stack = []
        i = 0
        ret = ""
        s = list(s)
        while i <= len(s) - 1:
            if s[i].isnumeric():
                tmp = int(s[i])
                i += 1
                while s[i].isnumeric():
                    tmp = tmp*10 + int(s[i])
                    i += 1
                stack.append(str(tmp))
            elif s[i] is '[':
                i += 1
            elif s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i] is ']':
                tmp_stack = []
                while True:
                    tmp = stack.pop()
                    if tmp.isnumeric():
                        stack.append(''.join(tmp_stack) * int(tmp))
                        break
                    else:
                        tmp_stack.insert(0, tmp)
                i += 1
        while len(stack) > 0:
            ret = str(stack.pop()) + ret
        print(ret)
        return ret

s = Solution()
s.decodeString("3[a]2[bc]")