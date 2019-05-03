class Solution(object):

    def validIPAddress(self, IP):

        def isIPv4(s):
            return s.isdigit() and str(int(s)) == s and 0 <= int(s) <= 255

        def isIPv6(s):
            return 0 < len(s) <= 4 and all(c in '0123456789abcdefABCDEF' for c in s) and int(s, 16) >= 0

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"

        return "Neither"
