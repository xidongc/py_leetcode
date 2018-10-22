class Solution(object):

    @staticmethod
    def min_steps(candy, n, m):
        min_step = float("inf")

        def dfs(curr, i, j, num_candy, steps):
            nonlocal min_step
            if num_candy == m:
                min_step = min(steps, min_step)

            if steps > min_step:
                return

            if (i, j) in candy:
                num_candy += 1

            if 0 <= i+1 < n and 0 <= j < n and (i+1, j) not in curr:
                curr.append((i+1, j))
                dfs(curr, i+1, j, num_candy, steps+1)
                curr.pop()

            if 0 <= i < n and 0 <= j-1 < n and (i, j-1) not in curr:
                curr.append((i, j-1))
                dfs(curr, i, j-1, num_candy, steps+1)
                curr.pop()

            if 0 <= j+1 < n and 0 <= i < n and (i, j+1) not in curr:
                curr.append((i, j+1))
                dfs(curr, i, j+1, num_candy, steps+1)
                curr.pop()

        dfs([], 0, 0, 0, 0)

        # need to -1 because last one should be exactly has candy, and in current
        # implementation, step+1 then find candy == m
        print(min_step-1)
        return min_step-1

candy = [(0, 3), (1, 1), (2, 2), (3, 3)]
m = len(candy)
n = 4

s = Solution()
s.min_steps(candy, n, m)
