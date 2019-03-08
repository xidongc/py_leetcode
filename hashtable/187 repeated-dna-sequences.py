# bit manipulation
# We also cannot store the 10-letter substrings themselves because they consume too much memory and the program will exceed memory limit.
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        subSet = set()
        dupSet = set()
        res = []
        map = {}
        map['A'] = 0
        map['C'] = 1
        map['G'] = 2
        map['T'] = 3
        # Here only four chars therefore using the bit manipulation to reduce the space

        for i in range(0, len(s) - 9):
            temp = 0
            for j in range(10):
                temp <<= 2
                temp |= map[s[j]]
            if not subSet.add(temp) and dupSet.add(temp):
                # if subSet.add(temp) == True dupSet.add(temp)would not be executed.
                res.append(s[i:j+1])
        return res

    # if not s or len(s) <= 10:
    #     return []
    # left, right = 0, 9
    # res = []
    # subList = []
    # while right < len(s):
    #     if s[left:right + 1] not in subList:
    #         subList.append(s[left:right + 1])
    #     else:
    #         res.append(s[left:right + 1])
    #     left += 1
    #     right += 1
    # return res


# public List<String> findRepeatedDnaSequences(String s) {
#     Set<Integer> words = new HashSet<>();
#     Set<Integer> doubleWords = new HashSet<>();
#     List<String> rv = new ArrayList<>();
#     char[] map = new char[26];
#     //map['A' - 'A'] = 0;
#     map['C' - 'A'] = 1;
#     map['G' - 'A'] = 2;
#     map['T' - 'A'] = 3;
#
#     for(int i = 0; i < s.length() - 9; i++) {
#         int v = 0;
#         for(int j = i; j < i + 10; j++) {
#             v <<= 2;
#             v |= map[s.charAt(j) - 'A'];
#         }
#         if(!words.add(v) && doubleWords.add(v)) {
#             rv.add(s.substring(i, i + 10));
#         }
#     }
#     return rv;
# }
s = Solution()
s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

