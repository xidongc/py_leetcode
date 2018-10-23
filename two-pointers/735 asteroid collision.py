#stack two pointers
# deque.append,appendleft,clear,reverse,count(n),remove(n)
import collections
# while ~ else
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        # 如果break出去了就不会返回到底下的else？
                        break
                    else:
                        break
                else:
                    # asteroid all the way to the left, hasn't been killed
                    stack.append(asteroid)
        return stack

s = Solution()
print(s.asteroidCollision([8,-8]))
