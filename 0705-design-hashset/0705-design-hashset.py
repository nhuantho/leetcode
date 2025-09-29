class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.head = ListNode(-1)

    def add(self, key: int) -> None:
        if self.contains(key):
            return 
        self.head.next = ListNode(key, self.head.next)

    def remove(self, key: int) -> None:
        prev, curr = None, self.head
        while curr:
            if curr.val == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False