# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = ""
        list = ListNode()

        if not head:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    head = curr1
                else:
                    head = curr2
            elif curr1:
                head = curr1
            else:
                head = curr2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                list.next = curr1
                curr1 = curr1.next

            else:
                list.next = curr2
                curr2 = curr2.next
            list = list.next

        if curr1:
            list.next = curr1

        if curr2:
            list.next = curr2

        return head


n1, n2, n3 = ListNode(1), ListNode(2), ListNode(4)
n1.next, n2.next, n3.next = n2, n3, None

n4, n5, n6 = ListNode(1), ListNode(3), ListNode(4)
n4.next, n5.next, n6.next = n5, n6, None

sol = Solution()
print(sol.mergeTwoLists(n1, n4).val)
