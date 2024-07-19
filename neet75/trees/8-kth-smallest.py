from typing import Optional
from collections import deque
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # maxHeap = []
        # stack = deque([root])

        # heapq.heapify(maxHeap)
        # while stack:
        #     curr = stack.pop()
        #     if curr:
        #         if len(maxHeap) < k:
        #             heapq.heappush(maxHeap, curr.val * -1)
        #         elif curr.val * -1 > maxHeap[0]:
        #             heapq.heappushpop(maxHeap, curr.val * -1)
        #         stack.append(curr.left)
        #         stack.append(curr.right)

        # return maxHeap[0] * -1

        stack = deque()
        curr = root
        list = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            list.append(curr.val)
            curr = curr.right
        return list[k - 1]
