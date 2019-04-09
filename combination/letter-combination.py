class Solution(object):

    def letterCombinations(self, digits: str):
        # corner case
        if len(digits) == 0:
            return list()

        letters = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def helper(stack, ret, digits, number):
            if len(stack) == number:
                ret.append("".join(stack))
                return

            elif len(stack) > number:
                return

            for i, d in enumerate(digits):
                for l in letters[int(d) - 1]:
                    stack.append(l)
                    helper(stack, ret, digits[i + 1:], number)
                    stack.pop()

        stack = list()
        ret = list()
        helper(stack, ret, digits, len(digits))
        return ret
