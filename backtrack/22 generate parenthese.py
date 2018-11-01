class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def generate(left,right,temp,res):
            if left > 0:
                generate(left - 1,right,temp + '(',res)
            #   if else只能执行一次，但是这里两个if独立
            if left < right:
                generate(left,right - 1,temp + ')', res)
            if left == 0 and right == 0:
                res.append(temp)
            
        generate(n,n,'',res)
        return res
#
# n = 3:
# [
#   "((()))",`
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
