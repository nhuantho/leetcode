# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        i, j = 0, len(nodes) - 1
        res = 0
        while i < j:
            res = max(res, nodes[i] + nodes[j])
            i += 1
            j -= 1
        
        return res