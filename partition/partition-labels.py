"""

While thinking abou this problem,
many might come up with a DP algorithm.
But this problem is much easier than DP problem.
First, scan the input string,
and store the maximum occurance index of every leter.
Then, scan the input string again,
considering the maximum occurance of each letter.While scanning,
if you encounter a letter whose maxium occurance index is larger than current,
update maximum occurance.
If the scanning index equals the maximum occurance index,
then we get a new break.

"""


class Solution:

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # S = "ababcbacadefegdehijhklij"
        ret = []

        map = {}
        # last = {c: i for i, c in enumerate(S)}
        for i, s in enumerate(S):
            map[s] = i

        partition = prev = 0
        for i, s in enumerate(S):

            partition = max(partition, map[s])

            if i == partition:
                ret.append(partition + 1 - prev)
                prev = partition + 1

        return ret


S = "eaaaabaaec"
s = Solution()
print(s.partitionLabels(S))

