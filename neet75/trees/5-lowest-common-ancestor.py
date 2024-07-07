from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.foundCount = 0

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if node:
                if node.val == p.val or node.val == q.val:
                    self.foundCount += 1
                if self.foundCount >= 2:
                    return True
                if node.left:
                    if dfs(node.left):
                        return True
                if node.right:
                    if dfs(node.right):
                        return True
            return False

        lowestNode = None

        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                self.foundCount = 0
                validSub = dfs(curr)
                if validSub:
                    lowestNode = curr
                queue.append(curr.left)
                queue.append(curr.right)

        return lowestNode
