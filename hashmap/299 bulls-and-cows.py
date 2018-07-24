class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        numa = 0
        numb = 0
        dicta = {}
        dictb = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                numa += 1
            else:
                dicta[secret[i]] = 1 if secret[i] not in dicta else dicta[secret[i]] + 1
                dictb[guess[i]] = 1 if guess[i] not in dictb else dictb[guess[i]] + 1
        for key in dicta.keys():
            if key in dictb:
                numb += min(dicta[key],dictb[key])
        return str(numa) + "A" + str(numb) + 'B'

s = Solution()
s.getHint("1807","7810")