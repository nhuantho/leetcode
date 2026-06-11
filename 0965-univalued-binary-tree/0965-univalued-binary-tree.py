# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.s_set = set()

        def dfs(node):
            if node is None:
                return
            
            self.s_set.add(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        if len(self.s_set) == 1:
            return True
        
        return False
        