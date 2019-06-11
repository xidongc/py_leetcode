# wish
class Solution(object):

    def FindFbSeries(self, input):
        # eg: input: "11235813"
        # corner case
        if len(input) < 3:
            return -1  # na

        ret = list()

        def dfs(stack, start):
            nonlocal ret
            if start == len(input):
                if len(stack) >= 3:
                    ret.append(stack[:])
                return

            for i in range(start, len(input)):
                if input[start] == "0" and i > start:
                    break

                if len(stack) < 2 or (len(stack) >= 2 and int(input[start:i+1]) == stack[-1] + stack[-2]):
                    stack.append(int(input[start:i+1]))
                    dfs(stack, i+1)
                    stack.pop()

        stack = list()
        dfs(stack, 0)

        return ret

s = Solution()
ret = s.FindFbSeries("011")
print(ret)