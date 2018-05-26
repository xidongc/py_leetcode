class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for _ in range(len(ratings))]
        total = len(ratings)

        for i in range(len(ratings) - 1):
            if ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                total += candies[i] + 1 - candies[i+1]
                candies[i+1] = candies[i] + 1
            if ratings[len(ratings)-i-2] > ratings[len(ratings)-i-1] and candies[len(ratings) - i - 2] <= candies[len(ratings) - i - 1]:
                total += candies[len(ratings) - i - 1] - candies[len(ratings) - i - 2] + 1
                candies[len(ratings) - i - 2] = candies[len(ratings) - i - 1] + 1

        return total

s = Solution()
ratings = [1,2,2]
print(s.candy(ratings))
