# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, num):
            if node is None:
                return

            num += str(node.val)

            if node is None:
                self.total += int(num)
                return

            if node.left is None and node.right is None:
                self.total += int(num)
                return

            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, "")

        return self.total
        