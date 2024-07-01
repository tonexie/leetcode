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

def print_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test cases
def test_reverse_list():
    # Test case 1: List: 1 -> 2 -> 3 -> 4 -> 5 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original list:")
    print_list(node1)

    sol = Solution()
    reversed_head = sol.reverseList(node1)

    print("Reversed list:")
    print_list(reversed_head)

test_reverse_list()
