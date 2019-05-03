class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # list to string
        if not num:
            return 'Zero'
        under20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
                   'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                   'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        to100 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def word(num):
            if num == 0:
                return []
            if num < 20:
                return [under20[num-1]]
            if num < 100:
                return [to100[num//10 - 2]] + word(num % 10)
            if num < 1000:
                return [under20[num//100 - 1]] + ['Hundred'] + word(num % 100)
            for pos, w in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if num < 1000**(pos+1):
                    return word(num//(1000**pos)) + [w] + word(num % (1000**pos))
        print(word(num))
        return ' '.join(word(num)).strip()


s = Solution()
print(s.numberToWords(50868))