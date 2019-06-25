import bisect


# TLE, using dfs recursion
class Solution(object):

    def minWindow(self, S: str, T: str) -> str:
        hashmap = dict()
        for i, s in enumerate(S):
            hashmap[s] = hashmap.get(s, list())
            hashmap[s].append(i)

        def dfs(startIndex, options, stack, ret):
            if len(stack) == len(T):
                ret.append(stack[:])
            elif len(stack) > len(T):
                return

            for i, option in enumerate(options):
                if option in hashmap:
                    newIndex = bisect.bisect_left(hashmap[option], startIndex + 1)
                    if newIndex == len(hashmap[option]):
                        return
                    for index in hashmap[option][newIndex:]:
                        stack.append(index)
                        dfs(index, options[i + 1:], stack, ret)
                        stack.pop()
                else:
                    return

        stack = list()
        ret = list()
        dfs(-1, T, stack, ret)
        ret.sort(key=lambda x: x[-1] - x[0])
        return S[ret[0][0]: ret[0][-1] + 1] if len(ret) > 0 else ""
