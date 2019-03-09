class Solution(object):

    def partition(self, s: str):
        if len(s) == 0:
            return [""]

        ret = list()
        stack = list()
        self.helper(s, stack, ret)
        return ret

    def helper(self, s, stack, ret):
        if len(s) == 0:
            ret.append(stack[:])
            return

        if len(s) < 0:
            return

        for j in range(1, len(s) + 1):
            if self.isPalindrome(s[0:j]):
                stack.append(s[0:j])
                self.helper(s[j:], stack, ret)
                stack.pop()

    def isPalindrome(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True
