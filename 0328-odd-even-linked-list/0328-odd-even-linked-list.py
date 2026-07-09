# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        o_n, e_n = None, None
        f_o_n, f_e_n = None, None
        i = 0
        while head:
            if i % 2 == 0:
                if e_n is None:
                    e_n = head
                    f_e_n = e_n
                else:
                    e_n.next = head
                    e_n = e_n.next
            else:
                if o_n is None:
                    o_n = head
                    f_o_n = o_n
                else:
                    o_n.next = head
                    o_n = o_n.next
            head = head.next
            i += 1

        o_n.next = None
        e_n.next = f_o_n
        return f_e_n
        