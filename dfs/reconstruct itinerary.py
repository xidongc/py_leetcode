class Solution(object):

    def findItinerary(self, tickets):

        dest = dict()
        length = len(tickets) + 1

        for ticket in tickets:
            tmp = dest.get(ticket[0], list())
            tmp.append(ticket[1])
            dest[ticket[0]] = tmp
            dest[ticket[1]] = dest.get(ticket[1], list())

        def dfs(start, stack):
            nonlocal dest, length
            if len(stack) == length:
                return stack
            if len(stack) > length:
                return

            dest[start].sort()
            for i, x in enumerate(dest[start]):
                stack.append(x)
                dest[start].pop(i)
                worked = dfs(x, stack)
                if worked:
                    return worked
                dest[start].insert(i, x)
                stack.pop()

        stack = ["JFK"]
        return dfs("JFK", stack)
