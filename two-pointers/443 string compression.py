class Solution(object):

    def compress(self, chars):

        if not chars:
            return 0

        # two pointers, one for iteration position, the other for modification pointer
        pos, mod = 0, 0

        while pos < len(chars):
            count = 0
            curChar = chars[pos]

            while pos < len(chars) and chars[pos] == curChar:
                count += 1
                pos += 1

            # two places to change, one to set char, one to set count
            chars[mod] = curChar
            mod += 1
            if count > 1:
                for c in str(count):
                    chars[mod] = c
                    mod += 1
        return mod
