# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([])

        q.append(root)

        self.res = []

        while q:
            l = len(q)

            for i in range(l):
                node = q.pop()

                if not node:
                    continue

                if i == l - 1:
                    self.res.append(node.val)
                
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

        return self.res
        