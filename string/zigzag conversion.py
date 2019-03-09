class Solution(object):
    def convert(self, s: str, numRows: int) -> str:

        def helper(s, numRows, arr):
            if len(s) == 0 or numRows <= 0:
                return

            elif numRows == 1:
                arr[0] = s
                return

            elif len(s) <= numRows:
                for i in range(len(s)):
                    arr[i] += s[i]
                return

            elif numRows < len(s) <= (numRows - 1) * 2:
                for i in range(numRows):
                    arr[i] += s[i]
                for i in range(len(s) - numRows):
                    arr[numRows - 2 - i] += s[i + numRows]
                return

            elif len(s) > (numRows - 1) * 2:
                for i in range(numRows):
                    arr[i] += s[i]
                for i in range(numRows - 2):
                    arr[numRows - 2 - i] += s[i + numRows]

            l = len(s)
            helper(s[numRows * 2 - 2:], numRows, arr)

        arr = ["" for _ in range(numRows)]
        helper(s, numRows, arr)
        return "".join(arr)