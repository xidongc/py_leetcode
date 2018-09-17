# 0, 1， 8转了一样
# 6，9互为reverse
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        for i in range((length + 1) // 2):
            if (num[i] in ['8', '1', '0'] and num[length - i - 1] == num[i]) or (
                    num[i] in ['6', '9'] and num[length - i - 1] in ['6', '9'] and num[i] != num[length - i - 1]):
                continue
            else:
                return False
        return True


