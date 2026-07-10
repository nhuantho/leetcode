# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_deep = 0
        def dfs(node, deep):
            if not node:
                return
            
            deep += 1
            
            self.max_deep = max(self.max_deep, deep)

            dfs(node.left, deep)
            dfs(node.right, deep)
        dfs(root, 0)
        return self.max_deep
        