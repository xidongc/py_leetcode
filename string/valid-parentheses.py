class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        openBracket = ["(", "[", "{"]
        closeBracket = [")", "]", "}"]
        dic = dict()

        for i, ele in enumerate(closeBracket):
            dic[ele] = openBracket[i]

        for ele in s:
            if ele in openBracket:
                stack.append(ele)
            elif ele in closeBracket:
                if len(stack) >= 1 and stack[-1] == dic.get(ele, None):
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False