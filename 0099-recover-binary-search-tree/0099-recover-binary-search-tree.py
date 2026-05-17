# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev

            if node is None:
                return
            
            inorder(node.left)

            if prev is not None and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            
            prev = node

            inorder(node.right)
        
        inorder(root)

        first.val, second.val = second.val, first.val
