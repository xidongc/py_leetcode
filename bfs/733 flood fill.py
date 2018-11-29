class Solution(object):
    def __init__(self):
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        # 如果color相同会导致死循环
        if oldColor != newColor:
            self.bfs(image, sr, sc,oldColor,newColor)
        return image
    def bfs(self, image, x, y, oldColor, newColor):
        image[x][y] = newColor
        for direction in self.directions:
            curx = x + direction[0]
            cury = y + direction[1]
            if curx >= 0 and cury >= 0 and curx < len(image) and cury < len(image[0]) and image[curx][cury] == oldColor:
                self.bfs(image, curx, cury, oldColor, newColor)
