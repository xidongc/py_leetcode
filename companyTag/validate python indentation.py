class Validate_Python_Indentation:
    def validate(self, lines):
        stack = []
        for line in lines:
            indent = self.getIndent(line)
            if not stack:
                if indent != 0:
                    return False
            else:
                if self.getIndent(stack[-1]) < indent:
                    if stack[-1][-1] != ':' or self.getIndent(stack[-1]) + 1 != indent:
                        return False
                else:
                    while self.getIndent(stack[-1]) > indent:
                        stack.pop()
                    if not stack or self.getIndent(stack[-1]) != indent:
                        return False
            stack.append(line)
        return True
    def getIndent(self, line):
        count = 0
        for c in line:
            if c == ' ':
                count += 1
            else:
                break
        return count / 4