# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaves1, self.leaves2 = [], []
        def dfs(node, l):
            if not node:
                return
            
            if not node.right and not node.left:
                l.append(node.val)
            
            dfs(node.left, l)
            dfs(node.right, l)
        
        dfs(root1, self.leaves1)
        dfs(root2, self.leaves2)

        if len(self.leaves1) == len(self.leaves2):
            for i in range(len(self.leaves1)):
                if self.leaves1[i] != self.leaves2[i]:
                    return False
            return True
        else:
            return False
        