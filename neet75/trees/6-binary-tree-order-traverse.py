from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])
        while queue:
            list = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    list.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if list:
                res.append(list)
        return res
