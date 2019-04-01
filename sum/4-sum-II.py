# LTE using two pointers O(n**3)
class Solution(object):

    def fourSumCount(self, A, B, C, D):
        # corner case:
        if len(A) == 0:
            return 0

        A.sort()
        B.sort()
        C.sort()
        D.sort()

        count = 0

        for i in range(len(A)):
            for j in range(len(B)):
                k = 0
                t = len(D) - 1

                while 0 <= k < len(C) and 0 <= t < len(D):
                    if A[i] + B[j] + C[k] + D[t] > 0:
                        t -= 1
                    elif A[i] + B[j] + C[k] + D[t] < 0:
                        k += 1
                    else:
                        tmp1 = 1
                        tmp2 = 1
                        while 0 <= k < len(C) - 1 and C[k + 1] == C[k]:
                            k += 1
                            tmp1 += 1
                        while 1 <= t < len(D) and D[t - 1] == D[t]:
                            t -= 1
                            tmp2 += 1
                        count += tmp1 * tmp2
                        k += 1
                        t -= 1

        return count


# hashmap Solution AC O(n**2)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashtable = {}
        count = 0
        for a in A:
            for b in B:
                if a+b in hashtable:
                    hashtable[a+b] += 1

                else:
                    hashtable[a+b] = 1

        for c in C:
            for d in D:
                if -c-d in hashtable:
                    count += hashtable[-c-d]
        return count