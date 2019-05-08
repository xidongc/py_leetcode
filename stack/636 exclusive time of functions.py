# rabbit sol
class Solution(object):

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        prevTime = 0
        for log in logs:
            func,status,time = log.split(":")
            func,time = int(func),int(time)
            if stack:
                res[stack[-1]] += time - prevTime
            # Set prevTime to current time
            prevTime = time
            if status == "start":
                stack.append(func)
                # current time belong to function:funcList[0]
            else:
                res[stack.pop()] += 1
                # current time belong to current function
                # prevTime start from the next time
                prevTime += 1
        return res


# mao mao sol
class Solution(object):

    def exclusiveTime(self, n, logs):
        stack = list()
        output = dict()
        tmp = logs[0].split(":")
        stack.append(int(tmp[0]))
        prev = int(tmp[2])

        for log in logs[1:]:
            tmp = log.split(":")
            if tmp[1] == "start":
                if len(stack) > 0:
                    output[stack[-1]] = output.get(stack[-1], 0) + int(tmp[2]) - prev
                stack.append(int(tmp[0]))
                prev = int(tmp[2])

            else:
                output[stack[-1]] = output.get(stack[-1], 0) + int(tmp[2]) - prev + 1
                stack.pop()
                prev = int(tmp[2]) + 1

        return list(output.values())
