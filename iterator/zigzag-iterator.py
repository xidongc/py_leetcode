class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.length = len(v1) + len(v2)
        self.position = 0

    def _next(self) -> int:
        if self.hasNext():
            if self.position % 2 == 0:
                if self.v1:
                    self.position += 1
                    return self.v1.pop(0)
                else:
                    self.position += 1
                    return self.v2.pop(0)
            elif self.position % 2 == 1:
                if self.v2:
                    self.position += 1
                    return self.v2.pop(0)
                else:
                    self.position += 1
                    return self.v1.pop(0)

    def hasNext(self) -> bool:
        return self.position < self.length
