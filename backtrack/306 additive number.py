# itertools.combinations(range(1, n), 2)
# str.startswith(prefix,pos)
# Array
import itertools
class Solution(object):

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i,j in itertools.combinations(range(1,len(num)),2):
            # 因为起码要有三个数，所以num2取不到num[j]
            num1 = num[:i]
            num2 = num[i:j]
            # 00,03          30,0
            if len(str(int(num1))) != len(num1) or len(str(int(num2))) != len(num2):
                continue
            while j < len(num):
                num3 = str(int(num1) + int(num2))
                if not num.startswith(num3,j):
                    break
                j += len(num3)
                if j == len(num):
                    return True
                num1,num2 = num2,num3
        return False
