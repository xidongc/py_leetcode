class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        head = 0

        while head is not None:
            head = self.reverseStrforK(s, k, head)

        return ''.join(s)

    def reverseStrforK(self, s, k, head):
        # head ... head+k-1...head+2k-1..(head+2k)
        p1 = head
        p2 = head
        if head+k-1 <= len(s) - 1:
            p2 = head+k-1
        else:
            p2 = len(s) - 1

        # reverse
        while p1 < p2:
            tmp = s[p1]
            s[p1] = s[p2]
            s[p2] = tmp
            p1 += 1
            p2 -= 1

        if head+2*k <= len(s) - 1:
            return head+2*k
        else:
            return None

s = "hello"
a = "sss"
print(s.join(a))
print(s.rstrip('o'))