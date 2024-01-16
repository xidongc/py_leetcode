class Vector2D(object):

    def __init__(self, vec2d):
        self.x = 0
        self.y = 0
        self.stack = vec2d
        self.next_item = None

    def next(self):
        return self.next_item

    def hasNext(self) -> bool:
        # Write your code here
        if self.x >= len(self.stack):
            return False
        curr = self.stack[self.x]
        while self.x < len(self.stack):
            if type(self.stack[self.x]) == int:
                self.next_item = self.stack[self.x]
                self.x += 1
                return True
            elif self.y < len(self.stack[self.x]):
                self.next_item = self.stack[self.x][self.y]
                self.y += 1
                return True
            else:
                self.x += 1
                self.y = 0
        self.next_item = None
        return False
