# suffix array building up
#  i	1	2	3	4	5	6	7
# S[i]	b	a	n	a	n	a	$

# first build suffix array begins with 1
# Suffix	i
# banana$	1
# anana$	2
# nana$	3
# ana$	4
# na$	5
# a$	6
# $	7

# then sort this array in lexicographically ascending order
# Suffix	i
# $	7
# a$	6
# ana$	4
# anana$	2
# banana$	1
# na$	5
# nana$	3

# for i in range(len-1)然后 compare suffix[i] and suffix[i+1],
# 从头开始的重复字符有多少

## Time complexity: O(nlogn), Space complexity: O(n)
## if using suffix tree, will take O(n) space and time
# import java.util.Arrays;
#
# public class LRS {
#
#     // return the longest common prefix of s and t
#     public static String lcp(String s, String t) {
#         int n = Math.min(s.length(), t.length());
#         for (int i = 0; i < n; i++) {
#             if (s.charAt(i) != t.charAt(i))
#                 return s.substring(0, i);
#         }
#         return s.substring(0, n);
#     }
#
#
#     // return the longest repeated string in s
#     public static String lrs(String s) {
#
#         // form the N suffixes
#         int N  = s.length();
#         String[] suffixes = new String[N];
#         for (int i = 0; i < N; i++) {
#             suffixes[i] = s.substring(i, N);
#         }
#  // sort them
#         Arrays.sort(suffixes);
#
#         // find longest repeated substring by comparing adjacent sorted suffixes
#         String lrs = "";
#         for (int i = 0; i < N - 1; i++) {
#             String x = lcp(suffixes[i], suffixes[i+1]);
#             if (x.length() > lrs.length())
#                 lrs = x;
#         }
#         return lrs;
#     }
#
#
#
#     // read in text, replacing all consecutive whitespace with a single space
#     // then compute longest repeated substring
#     public static void main(String[] args) {
#         String s = StdIn.readAll();
#         s = s.replaceAll("\\s+", " ");
#         StdOut.println("'" + lrs(s) + "'");
#     }
# }
