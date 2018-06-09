class Solution(object):
    def __init__(self, a):
        self.a = a

s = Solution(1)
b = s
b.a = 2
print(s.a)
print(id(s))
print(id(b))





