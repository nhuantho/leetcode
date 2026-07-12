# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(node, total, cache):
            if not node:
                return
            
            total += node.val
            check_val = total - targetSum
            self.res += cache.get(check_val, 0)
            cache[total] = cache.get(total, 0) + 1

            dfs(node.left, total, cache)
            dfs(node.right, total, cache)

            cache[total] -= 1
            
        
        dfs(root, 0, {0:1})

        return self.res

            
