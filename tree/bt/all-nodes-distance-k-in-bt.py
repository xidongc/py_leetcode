from collections import deque


class Solution:
    """
    using dfs to find parent
    using bfs to find distance == k ele including parents
    """
    def distanceK(self, root, target, K):
        if root is None:
            return []

        parents = {}
        queue = deque([target])
        visited = {target}
        distance = 0
        self.build_parents(root, parents)

        while queue and distance < K:
            for _ in range(len(queue)):
                node = queue.popleft()

                # Find adjacent
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parents and parents[node] not in visited:
                    queue.append(parents[node])
                    visited.add(parents[node])

            distance += 1

        return [node.val for node in queue]

    def build_parents(self, root, parents):
        if root is None:
            return None

        if root.left:
            parents[root.left] = root
            self.build_parents(root.left, parents)
        if root.right:
            parents[root.right] = root
            self.build_parents(root.right, parents)
