from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root):
            stack = deque([root])
            list = []
            while stack:
                curr = stack.pop()
                if curr:
                    list.append(curr.val)
                    stack.append(curr.left)
                    stack.append(curr.right)
                else:
                    list.append("null")
            return list

        list1 = dfs(p)
        list2 = dfs(q)
        print(list1)
        print(list2)

        if list1 == list2:
            return True
        return False
