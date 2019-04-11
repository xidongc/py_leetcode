class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return 0
        if len(a) > len(b):
            b = "0"*(len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0"*(len(b) - len(a)) + a
        carry = False
        res = ""
        for i in range(len(a) - 1, -1, -1):
            if a[i] == b[i] == "1":
                if carry: 
                    res = "1" + res
                else:
                    res = "0" + res
                    carry = True
            elif a[i] == "1" or b[i] == "1":
                if carry:
                    res = "0" + res
                else:
                    res = "1" + res
            else:
                if carry:
                    res = "1" + res
                    carry = False
                else:
                    res = "0" + res
        
        return res if not carry else "1" + res
        # Input: a = "11", b = "1"
        # Output: "100"


class Solution(object):

    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a

        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a

        # a and b has same length
        a = list(map(int, a))
        b = list(map(int, b))
        carrier = 0
        result = ""

        for i in range(len(a)):
            result = str((a[len(a) - 1 - i] + b[len(a) - 1 - i] + carrier) % 2) + result
            carrier = (a[len(a) - 1 - i] + b[len(a) - 1 - i] + carrier) // 2

        if carrier == 1:
            result = "1" + result
        return result
