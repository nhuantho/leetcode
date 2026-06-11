# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_d, self.y_d, self.x_p, self.y_p = None, None, None, None
        def dfs(node, p_node, depth):
            if node is None:
                return
            
            if node.val == x:
                self.x_d = depth
                self.x_p = p_node
            
            if node.val == y:
                self.y_d = depth
                self.y_p = p_node
            
            depth += 1

            dfs(node.left, node, depth)
            dfs(node.right, node, depth)

        dfs(root, None, 0)

        if self.y_d == self.x_d and self.x_p != self.y_p:
            return True
        
        return False


        