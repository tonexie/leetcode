from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxDepth = 0
        # queue = deque([(root, 1)])
        # while queue:
        #     curr = queue.popleft()
        #     if curr[0]:
        #         depth = curr[1]
        #         if curr[0].left or curr[0].right:
        #             depth += 1
        #         maxDepth = max(maxDepth, depth)
        #         queue.append((curr[0].left, depth))
        #         queue.append((curr[0].right, depth))
        # return maxDepth

        maxDepth = 0
        queue = deque([root])
        while queue and root:
            maxDepth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return maxDepth
