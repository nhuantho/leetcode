# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum_val = 0
        def dfs(node):
            if node is None:
                return
            
            if node.left and node.left.left is None and node.left.right is None:
                self.sum_val += node.left.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.sum_val
        