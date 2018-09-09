# design
# 好难理解啊
# 找小本本

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        # Since it could be ['a','b','c',''] or ['','b','c','']]
        self.tmp = [""] * 4
        self.head = 0
        self.tail = 0
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while count < n:
            if self.head == self.tail:
                self.tail = read4(self.tmp)
                self.head = 0
                if not self.tail:
                    break
            while self.head < self.tail and count < n:
                buf[count] = self.tmp[self.head]
                count += 1
                self.head += 1
        return count




