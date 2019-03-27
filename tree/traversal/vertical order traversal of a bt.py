from collections import defaultdict


class Solution(object):

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # corner case
        if root is None:
            return list()

        queue = list()  # deque faster
        queue.append((root, 0, 0))
        seen = list()

        while len(queue) > 0:
            curr, x, y = queue.pop()
            seen.append((curr.val, x, y))
            if curr.left:
                queue.append((curr.left, x - 1, y + 1))
            if curr.right:
                queue.append((curr.right, x + 1, y + 1))

        seen.sort(key=lambda x: (x[1], x[2], x[0]))
        seen = [(x[1], x[0]) for x in seen]
        ret = defaultdict(list)
        for s in seen:
            ret[s[0]].append(s[1])
        result = list()
        for x in ret.values():
            result.append(x)
        return result
