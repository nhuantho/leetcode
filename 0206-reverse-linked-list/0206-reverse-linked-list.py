# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        tail = dummy

        list_value = []
        while head:
            list_value.append(head.val)
            head = head.next
        cnt = len(list_value) - 1

        while cnt >= 0:
            tail.next = ListNode(list_value[cnt])
            tail = tail.next
            cnt -= 1
        return dummy.next