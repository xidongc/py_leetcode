class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        Solution.res= []
        self.backtrack(0, 0, 0, [],S)
        return Solution.res
    def backtrack(self, start, last1, last2, intList, string):

        for i in range(start,len(string)):
            cur = int(string[start:i + 1])
            if len(string[start:i + 1]) != len(str(cur)):
                break
            # if cur > 2147483647:
            #     break
            if len(intList) == 0:
                self.backtrack(i + 1, cur, last2, intList + [cur], string)
            elif len(intList) == 1:
                self.backtrack(i + 1, last1, cur, intList + [cur], string)
            else:
                if cur > last1 + last2:
                    break
                elif cur == last1 + last2:
                    if i == len(string) - 1:
                        Solution.res = intList + [cur]
                        return
                    else:
                        self.backtrack(i + 1, last2, cur, intList + [cur], string)
                else:
                    continue

s = Solution()
print(s.splitIntoFibonacci("123456579"))