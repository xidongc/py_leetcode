# yelp
import random
import collections

class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.cDict = collections.defaultdict(int)
        self.cList = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):

        """
        @param: server_id: server_id remove a bad server from the cluster
        @return: nothing
        """
        self.cList.append(server_id)
        self.cDict[server_id] = len(self.cList) - 1


    def remove(self, server_id):
        # write your code here

        # O(1)时间查找，index函数并不行，需要用dict
        pos = self.cDict[server_id]
        lastNum = self.cList[-1]
        if lastNum != server_id:
            self.cList[pos] = lastNum
            self.cDict[lastNum] = pos
        self.cList.pop()
        del self.cDict[server_id]

    def pick(self):
        """
        @return: pick a server in the cluster randomly with equal probability
        """
        if self.cList:
            return random.choice(self.cList)
        # return self.nums[random.randint(0, len(self.nums) - 1)]
        else:
            return -1
s = LoadBalancer()
s.add(1)
s.add(2)
s.add(3)
print(s.pick())
print(s.pick())
print(s.pick())
s.remove(1)
print(s.pick())
print(s.pick())
