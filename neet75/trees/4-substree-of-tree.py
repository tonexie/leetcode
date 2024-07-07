from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(rootNode):
            stack = deque([rootNode])
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
        
        subRootList = dfs(subRoot)
        queue = deque([root])
        while queue:
          curr = queue.popleft()
          if curr:
            if curr.val == subRoot.val:
              subList = dfs(curr)
              if subList == subRootList:
                return True
            queue.append(curr.left)
            queue.append(curr.right)
        
        return False
              
