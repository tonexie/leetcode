class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def dfs(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                dfs(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                dfs(openCount, closeCount + 1)
                stack.pop()

        dfs(0, 0)
        return res
