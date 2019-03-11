import collections



class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            cur = queue.pop(0)
            for i in range(4):
                x = cur[0] + directions[i][0]
                y = cur[1] + directions[i][1]
                if x >= 0 and x < len(rooms) and y >= 0 and y < len(rooms[0]) and rooms[x][y] == 2147483647:
                    queue.append((x, y))
                    rooms[x][y] = rooms[cur[0]][cur[1]] + 1





