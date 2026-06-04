# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.values = []
        def dfs(node):
            if node is None:
                return
            
            self.values.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        new_values = list(set(self.values))
        if len(new_values) <= 1:
            return -1
        new_values.sort()
        return new_values[1]