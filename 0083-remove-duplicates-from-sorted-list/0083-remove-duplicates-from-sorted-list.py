# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        tail = dummy

        tail.next = ListNode(head.val)
        tail = tail.next
        head = head.next
        while head:
            if head.val != tail.val:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next

        return dummy.next