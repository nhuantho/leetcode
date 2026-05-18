# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, total, path):
            if node is None:
                return

            total += node.val
            path.append(node.val)

            if total == targetSum and node.left is None and node.right is None:
                res.append(path.copy())

            dfs(node.left, total, path)
            dfs(node.right, total, path)

            path.pop()

        dfs(root, 0, [])
        return res
        