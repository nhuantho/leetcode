class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.head = ListNode(-1, -1)

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.head.next = ListNode(key, value, self.head.next)

    def get(self, key: int) -> int:
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        prev, curr = self.head, self.head.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next