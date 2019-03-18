class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False

        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            n = str(n)
            tmp = [int(x) * int(x) for x in n]
            n = sum(tmp)

        if n in visited:
            return False
        elif n == 1:
            return True