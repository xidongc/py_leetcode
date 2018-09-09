# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # Case1: n > len(string), flag first changes
        # Case2: n < len(string), total first reaches n
        tmp = [""] * 4
        total = 0
        flag = False
        # flag becomes True also when total cannot reach n(n > len(string))
        while not flag and total < n:
            count = read4(tmp)
            # reaches the end of string
            flag = count < 4
            count = min(count, n - total)
            for i in range(count):
                buf[total] = tmp[i]
                total += 1
        return total