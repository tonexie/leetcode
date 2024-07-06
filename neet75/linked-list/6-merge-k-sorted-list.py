from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        id = 0
        curr = dummy
        minHeap = []
        heapq.heapify(minHeap)
        for node in lists:
            if node:
                heapq.heappush(minHeap, [node.val, id, node])
                id += 1

        while minHeap:
            heapList = heapq.heappop(minHeap)
            minNode = heapList[2]
            curr.next = minNode
            curr = curr.next
            minNode = minNode.next
            if minNode:
                heapq.heappush(minHeap, [minNode.val, id, minNode])
                id += 1

        return dummy.next


# def printList(head):
#     curr = head
#     print("-----")
#     while curr:
#         print(curr.val)
#         curr = curr.next
#     print("-----")


# # n1 = ListNode(1, ListNode(2, ListNode(4)))
# # n2 = ListNode(2, ListNode(3, ListNode(5)))
# # n3 = ListNode(3, ListNode(6))
# n1 = None
# sol = Solution()
# printList(sol.mergeKLists([n1]))


# class Solution:

#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists or len(lists) == 0:
#             return None

#         while len(lists) > 1:
#             mergedLists = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if (i + 1) < len(lists) else None
#                 mergedLists.append(self.mergeList(l1, l2))
#             lists = mergedLists
#         return lists[0]

#     def mergeList(self, l1, l2):
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2
#         return dummy.next
