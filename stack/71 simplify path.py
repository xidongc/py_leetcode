class Solution(object):

    def simplifyPath(self, path: str) -> str:

        # corner case
        if len(path) == 0:
            return ""

        places = [p for p in path.split("/") if p != "." and p != ""]
        stack = list()

        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
