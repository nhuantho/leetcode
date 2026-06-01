# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        def dfs(node):
            if node is None:
                return
            
            self.values.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        self.values.sort()
        return self.values[k-1]
        