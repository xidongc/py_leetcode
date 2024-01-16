class Solution:

    def daily_temperatures(self, temperatures):
        # mono stack left -> right
        results = [0] * len(temperatures)
        mono_stack = []
        for i, temperature in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < temperature:
                ele = mono_stack.pop()
                results[ele] = i - ele
            mono_stack.append(i)
        return results
