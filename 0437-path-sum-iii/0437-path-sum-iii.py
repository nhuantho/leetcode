# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(node, curr_path_sum, cache):
            if not node:
                return
            
            curr_path_sum += node.val
            old_path_sum = curr_path_sum - targetSum
            self.res += cache.get(old_path_sum, 0)
            cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

            dfs(node.left, curr_path_sum, cache)
            dfs(node.right, curr_path_sum, cache)

            cache[curr_path_sum] -= 1
        
        dfs(root, 0, {0:1})
        return self.res

            
