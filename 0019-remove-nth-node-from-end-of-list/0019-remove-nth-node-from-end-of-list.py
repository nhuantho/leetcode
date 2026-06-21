# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_head = []
        while head:
            list_head.append(head.val)
            head = head.next
        
        l = len(list_head)

        node = None
        res = None
        for i in range(l):
            if i != l - n:
                if node is None:
                    node = ListNode(list_head[i])
                    res = node
                else:
                    node.next = ListNode(list_head[i])
                    node = node.next

        return res