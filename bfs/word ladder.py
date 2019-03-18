import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        # corner case
        if endWord not in wordList:
            return 0

        if len(wordList) == 0:
            return 1 if endWord is beginWord else 0

        # bfs level traversal
        queue = list()  # use deque, which is faster
        queue.append(beginWord)
        level = 1
        visited = set()
        wordList = set(wordList)

        while len(queue) > 0:
            length = len(queue)
            for _ in range(length):
                curr = queue.pop(0)
                for i, ele in enumerate(curr):
                    for j in list(string.ascii_lowercase):
                        tmp = curr[:i] + j + curr[i + 1:]
                        if tmp in wordList and tmp not in visited:
                            queue.append(tmp)
                            visited.add(tmp)
                            if tmp == endWord:
                                return level + 1
            level += 1
        return 0
