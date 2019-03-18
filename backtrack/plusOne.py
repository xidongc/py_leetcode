class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return list()

        i = len(digits) - 1
        tmp = (digits[i] + 1) % 10
        digits[i] = tmp
        while i > 0 and tmp == 0:
            i -= 1
            tmp = (digits[i] + 1) % 10
            digits[i] = tmp
        if tmp == 0:
            digits.insert(0, 1)
        return digits
