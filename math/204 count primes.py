class Solution(object):

    def countPrimes(self, n: int) -> int:

        # corner case
        if n <= 1:
            return 0

        visited = [True for _ in range(n)]
        visited[0] = False
        visited[1] = False

        for x in range(2, n):
            if visited[x]:
                t = 2
                while t * x < n:
                    visited[t * x] = False
                    t += 1

        return len([x for x in visited if x is True])
