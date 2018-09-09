class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #         i = 0
        # #         s = s.trim();
        #         s = s.strip() + " ";
        #         length = len(s) - 1
        #         if s[i] == '+' or s[i] == '-':
        #             i += 1
        #         nDigit = 0
        #         nPoint = 0
        #         while s[i].isdigit() or s[i] == '.':
        #             if s[i].isdigit():
        #                 nDigit += 1
        #             if s[i] == '.':
        #                 nPoint += 1
        #             i += 1
        #         if nDigit <= 0 or nPoint > 1:
        #             return False
        #         if s[i] == 'e':
        #             i += 1
        #             if s[i] == '+' or s[i] == '-':
        #                 i += 1
        #             if i == length:
        #                 return False
        #             while i < length:
        #                 if not s[i].isdigit():
        #                     return False
        #                 i += 1
        #         return i == length

        # 先去判断是否general符合，遇到e再去判断右边
        # 防止overflow，这样只用检验是否到达最后这个space的位置即可
        s = s.strip() + ' '
        length = len(s) - 1
        i = 0
        digitNum = 0
        dotNum = 0
        if s[i] == '+' or s[i] == '-':
            i += 1
        while s[i].isdigit() or s[i] == '.':
            digitNum += 1 if s[i].isdigit() else 0
            dotNum += 1 if s[i] == '.' else 0
            i += 1
        if digitNum < 1 or dotNum > 1:
            return False
        if s[i] == 'e':
            i += 1
            if s[i] == '+' or s[i] == '-':
                i += 1
            if i == length:
                return False
            while i < length:
                if not s[i].isdigit():
                    return False
                i += 1
        return i == length

