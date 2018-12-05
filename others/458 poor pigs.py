class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
# 一只猪鉴定5桶，2两只猪一只喝行一只喝列能喝25桶，三只猪一只行一只列一只面
# 真无聊什么鬼题
#         什么有毒猪种还从0开始没有猪哪里能鉴定
        
        pigNum = 0
        while (minutesToTest // minutesToDie + 1) ** pigNum < buckets:
            pigNum += 1
        return pigNum