class Solution:

    def restoreIpAddresses(self, s: str):
        results = []

        def helper(i: int, result: list):
            nonlocal results, s
            if len(result) == 4:
                if i == len(s):
                    results.append(".".join(result))
                return
            elif len(result) > 4 or i >= len(s):
                return

            if i == len(s) - 1 or s[i] == '0':
                result.append(s[i])
                helper(i + 1, result)
                result.pop()
            elif len(s) - i >= 3 and 0 < int(s[i:i + 3]) <= 255:
                for length in range(1, 4):
                    result.append(s[i:i + length])
                    helper(length + i, result)
                    result.pop()
            else:
                for length in range(1, 3):
                    result.append(s[i:i + length])
                    helper(i + length, result)
                    result.pop()

        helper(0, [])
        return results


# 468 validate ip address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ins = []
        if "." in IP:
            try:
                ins = IP.split(".")
                if len(ins) != 4:
                    return "Neither"
            except Exception as ex:
                return "Neither"
        elif ":" in IP:
            try:
                ins = IP.split(":")
                if len(ins) != 8:
                    return "Neither"
            except Exception as ex:
                return "Neither"

        if len(ins) == 4:
            return "IPv4" if self.isipv4(ins) else "Neither"
        elif len(ins) == 8:
            return "IPv6" if self.isipv6(ins) else "Neither"
        return "Neither"

    def isipv4(self, s: list) -> bool:
        print(s)
        for si in s:
            try:
                inp = int(si)
                if inp > 255 or inp < 0 or (len(si) > 1 and si[0] == '0'):
                    return False
            except Exception as ex:
                return False
        return True

    def isipv6(self, s: list) -> bool:
        for si in s:
            if len(si) < 1 or len(si) > 4:
                return False
            for a in si:
                if not a.isdigit() and not a.isalpha():
                    return False
                elif a.isalpha() and not (ord('a') <= ord(a) <= ord('f')) and not (ord('A') <= ord(a) <= ord("F")):
                    return False
        return True
