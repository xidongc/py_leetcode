class Solution(object):

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        elif n == 2:
            return x * x
        elif n == 1:
            return x
        elif n == 0:
            return 1
        elif n % 2 == 0:
            return self.myPow(self.myPow(x, n // 2), 2)
        elif n % 2 == 1:
            return self.myPow(self.myPow(x, n // 2), 2) * x
        else:
            print("something's wrong")
