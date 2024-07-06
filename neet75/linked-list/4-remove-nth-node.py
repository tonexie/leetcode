from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, count = 0, 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        nth = head
        while count < length - n - 1:
            nth = nth.next
            count += 1

        print(length)
        print(count)
        
        if length - n == 0:
          head = head.next
        elif not nth.next.next:
          nth.next = None
        else:
          nth.next = nth.next.next
        return head


def printList(head):
    print("-----")
    node = head
    while node:
        print(node.val)
        node = node.next
    print("-----")


# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(1, ListNode(2))
sol = Solution()
printList(sol.removeNthFromEnd(head, 2))
