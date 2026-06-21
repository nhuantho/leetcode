# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_head = []
        tmp = head
        while tmp:
            list_head.append(tmp)
            tmp = tmp.next
        
        l = len(list_head)

        if n == l:
            return head.next

        list_head[l - n - 1].next = list_head[l - n].next
        
        return head