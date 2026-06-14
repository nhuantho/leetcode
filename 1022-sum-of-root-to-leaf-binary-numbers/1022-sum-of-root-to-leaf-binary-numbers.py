# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(node, num_bin):
            if node is None:
                return

            num_bin = num_bin + str(node.val)

            if node.left is None and node.right is None:
                self.total += int(num_bin, 2)
            
            dfs(node.left, num_bin)
            dfs(node.right, num_bin)
        
        dfs(root, "")
        return self.total
        