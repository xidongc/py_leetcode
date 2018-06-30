class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = len(num1) + len(num2)
        product = [0 for i in range(length)]
        pos = len(product) - 1
        for n1 in num1[::-1]:
            tempPos = pos
            for n2 in num2[::-1]:
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] // 10
                product[tempPos] = product[tempPos] % 10
                tempPos -= 1
            pos -= 1
        rmPos = 0
        while rmPos < len(product) - 1 and product[rmPos] == 0:
            rmPos += 1
        return ''.join(map(str, product[rmPos:]))
# Input: num1 = "2", num2 = "3"
# Output: "6"
