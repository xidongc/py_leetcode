class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        p1 = p2 = 0
        hash_set = {}
        max_length = 0
        
        while p2 <= len(s)-1:
            if s[p2] not in hash_set or hash_set[s[p2]] < p1:
                hash_set[s[p2]] = p2
                max_length = max(max_length, p2 - p1 + 1)
                p2 += 1
            else:
                p1 = hash_set[s[p2]] + 1
                hash_set[s[p2]] = p2
                p2 += 1
                
        return max_length

s = Solution()
string = "tmmzuxt"
print(s.lengthOfLongestSubstring(string))