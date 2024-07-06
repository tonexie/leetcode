class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        node = s.next
        s.next = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        new = head
        while prev:
            temp1 = new.next
            temp2 = prev.next
            new.next = prev
            prev.next = temp1
            prev = temp2
            new = temp1

        return head


# Helper function to print the list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
sol.reorderList(head)
printList(head)  # Expected output: 1 -> 5 -> 2 -> 4 -> 3 -> None
