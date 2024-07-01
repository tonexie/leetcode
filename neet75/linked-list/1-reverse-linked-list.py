from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move to the next node in the original list
        return prev  # Prev will be the new head of the reversed list
