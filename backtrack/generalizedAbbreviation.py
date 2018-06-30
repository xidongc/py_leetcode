class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        Solution.res = []
        self.helper(word,"",0,0)
        return Solution.res
    def helper(self,word,temp,pos,count):
        if pos == len(word):
            temp = temp + str(count) if count > 0 else temp
            Solution.res.append(temp)
        else:
            self.helper(word,temp,pos + 1,count + 1)
            self.helper(word,temp + (str(count) if count > 0 else "") + word[pos],pos + 1,0)
#Input: "word"
#Output:
#["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#我觉得这题非常好
