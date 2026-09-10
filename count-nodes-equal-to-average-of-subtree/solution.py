class Solution:
    def averageOfSubtree(self, root) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            s, c = ls + rs + node.val, lc + rc + 1
            if s // c == node.val:
                self.count += 1
            return (s, c)
        dfs(root)
        return self.count
