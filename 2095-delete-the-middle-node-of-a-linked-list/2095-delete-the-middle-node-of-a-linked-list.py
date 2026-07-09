# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        
        n = len(nodes)

        if n == 1:
            return None
        
        if n == 2:
            head.next = None
            return head
        
        i_m = n // 2

        nodes[i_m - 1].next = nodes[i_m + 1]
        return head
        
