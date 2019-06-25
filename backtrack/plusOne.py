class Solution(object):

    def plusOne(self, digits):
        # corner case
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


# Sol-2 by xidong
class Solution(object):

    def plusOne(self, digits):
        # corner case
        if len(digits) == 0:
            return -1  # not applicable

        carrier = 0
        ret = list()

        for i, d in enumerate(digits[::-1]):
            if i == 0:
                tmp = d + 1 + carrier
            else:
                tmp = d + carrier
            d = tmp % 10
            carrier = tmp // 10
            ret.append(d)
        if carrier == 1:
            ret.append(1)
        ret.reverse()
        return ret
