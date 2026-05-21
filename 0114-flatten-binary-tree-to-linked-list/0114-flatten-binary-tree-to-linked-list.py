# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def dfs(node):
            if node is None:
                return

            right_tail = dfs(node.right)
            left_tail = dfs(node.left)

            tmp = node.right

            if node.left:
                node.right = node.left
                node.left = None

                left_tail.right = tmp
            
            if right_tail:
                return right_tail
            
            if left_tail:
                return left_tail

            return node
        
        dfs(root)