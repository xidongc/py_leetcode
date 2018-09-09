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