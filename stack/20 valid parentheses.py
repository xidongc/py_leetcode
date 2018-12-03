class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                    continue
                else:
                    return False
        return len(stack) == 0
# ['(']