class Solution(object):

    def decodeString(self, s):
        # Input: S = abc3[a]
        # Output: "abcaaa"

        stack = []
        tmp = 0
        for i in range(len(s)):
            if s[i].isdigit():
                tmp = tmp * 10 + int(s[i])
            elif s[i] == "[":
                stack.append(str(tmp))
                tmp = 0
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i] == "]":
                letters = ""
                while stack and not stack[-1].isdigit():
                    letters = stack.pop() + letters
                if stack:
                    letters *= int(stack.pop())
                stack.append(letters)

        return "".join(stack)
