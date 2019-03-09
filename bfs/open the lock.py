from collections import deque


class Solution(object):

    # previously LTE, change list to deque, which is found in
    # https://leetcode.com/problems/open-the-lock/discuss/110232/Accepted-PythonJava-BFS-%2B-how-to-avoid-TLE
    def openLock(self, deadends, target):

        # corner case
        if "0000" in deadends:
            return -1

        lock = [i for i in range(10)]
        queue = deque()
        ret = 0
        positions = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
                     (-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)]
        visited = set()
        visited.add((0, 0, 0, 0))
        queue.append((0, 0, 0, 0))

        while len(queue) > 0:
            length = len(queue)
            for _ in range(length):
                (i, j, k, t) = queue.popleft()
                if str(lock[i]) + str(lock[j]) + str(lock[k]) + str(lock[t]) == target:
                    return ret

                for (di, dj, dk, dt) in positions:
                    if self.in_boundary(i + di, j + dj, k + dk, t + dt) and str(lock[i + di]) + str(lock[j + dj]) + str(
                            lock[k + dk]) + str(lock[t + dt]) not in deadends and (
                    i + di, j + dj, k + dk, t + dt) not in visited:
                        queue.append((i + di, j + dj, k + dk, t + dt))
                        visited.add((i + di, j + dj, k + dk, t + dt))
            ret += 1
        return -1

    def in_boundary(self, x, y, z, t):
        return -10 <= x <= 9 and -10 <= y <= 9 and -10 <= z <= 9 and -10 <= t <= 9