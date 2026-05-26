# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        if root is None:
            return res

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                if prev is None:
                    res.append(queue[-1].val)

                node = queue.popleft()

                if node is None:
                    continue

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            prev = None

        return res


