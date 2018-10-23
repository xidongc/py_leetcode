from collections import Counter
from queue import PriorityQueue


class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = Counter(tasks)
        p = PriorityQueue()
        for k, v in dic.items():
            p.put((-v,k))

        l = len(tasks)*(n+1)
        matrix = [False]*l

        while not p.empty():
            number = dic[p.get()[1]]
            dis = -n-1
            for i in range(l):
                if number > 0 and matrix[i] is False and i-dis > n:
                    matrix[i] = True
                    number -= 1
                    dis = i
                if number == 0:
                    break

        print(matrix)

        i = l-1
        while matrix[i] is not True:
            i -= 1
        print(i+1)
        return i+1




s = Solution()
s.leastInterval(["G","C","A","H","A","G","G","F","G","J","H","C","A","G","E","A","H","E","F","D","B","D","H","H","E","G","F","B","C","G","F","H","J","F","A","C","G","D","I","J","A","G","D","F","B","F","H","I","G","J","G","H","F","E","H","J","C","E","H","F","C","E","F","H","H","I","G","A","G","D","C","B","I","D","B","C","J","I","B","G","C","H","D","I","A","B","A","J","C","E","B","F","B","J","J","D","D","H","I","I","B","A","E","H","J","J","A","J","E","H","G","B","F","C","H","C","B","J","B","A","H","B","D","I","F","A","E","J","H","C","E","G","F","G","B","G","C","G","A","H","E","F","H","F","C","G","B","I","E","B","J","D","B","B","G","C","A","J","B","J","J","F","J","C","A","G","J","E","G","J","C","D","D","A","I","A","J","F","H","J","D","D","D","C","E","D","D","F","B","A","J","D","I","H","B","A","F","E","B","J","A","H","D","E","I","B","H","C","C","C","G","C","B","E","A","G","H","H","A","I","A","B","A","D","A","I","E","C","C","D","A","B","H","D","E","C","A","H","B","I","A","B","E","H","C","B","A","D","H","E"]
,1)



