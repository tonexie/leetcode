from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # while curr:
        #     if curr.val == "marked":
        #         return True
        #     curr.val = "marked"
        #     curr = curr.next
        # return False

        # hashSet = set()
        # curr = head
        # while curr:
        #     if curr in hashSet:
        #         return True
        #     hashSet.add(curr)
        #     curr = curr.next
        # return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
