# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        n, num = len(arr), 0
        for i in range(n):
            num = num + 2**(n-1-i) * arr[i]
        return num
        