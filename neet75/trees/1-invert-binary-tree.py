from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # queue = deque([root])
        # while queue:
        #     curr = queue.popleft()
        #     if curr:
        #         temp = curr.left
        #         curr.left = curr.right
        #         queue.append(curr.left)
        #         curr.right = temp
        #         queue.append(curr.right)
                
        # return root

        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
