class StockSpanner:
    def __init__(self):
        self.stack = []
        self.position = 0
        self.prices = []

    """
    @param price: 
    @return: int
    """

    def next(self, price):
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        tmp = self.position - self.stack[-1][1] if self.stack else self.position + 1
        self.stack.append((price, self.position))
        self.position += 1
        return tmp
