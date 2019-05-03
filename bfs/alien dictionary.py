class Solution(object):

    def alienOrder(self, words: List[str]) -> str:
        # corner case
        if len(words) == 0:
            return ""

        rel = dict()
        indegree = dict()

        for word in words:
            for w in word:
                indegree[w] = 0
                rel[w] = set()

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] != words[i - 1][j]:
                    if words[i][j] not in rel[words[i - 1][j]]:
                        indegree[words[i][j]] += 1
                        rel[words[i - 1][j]].add(words[i][j])
                    break

        queue = list()
        output = list()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
                output.append(k)

        while len(queue) > 0:
            curr = queue.pop(0)
            if curr in rel:
                for x in rel[curr]:
                    if x in indegree:
                        indegree[x] -= 1
                        if indegree[x] == 0:
                            queue.append(x)
                            output.append(x)

        return "".join(output) if len(output) == len(indegree) else ""
