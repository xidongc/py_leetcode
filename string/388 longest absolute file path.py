# 因为\t是特殊字符，所以\t在len中只会算单个字符
# 前缀和数组
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        res = 0
        sum = [0 for i in range(len(input)+1)]
        for string in input.split('\n'):
            level = string.count("\t") + 1
            length = len(string) - (level - 1)
            if "." in string:
                # file path, empty folder的长度不用计算
                res = max(res,sum[level-1]+length)
            else:
                # 若重新开始一个level，会把前面覆盖掉
                # dir\,加上dash的长度
                sum[level] = sum[level-1] + length + 1
        return res
string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
s = Solution()
s.lengthLongestPath(string)
