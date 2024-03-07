class MinStack(object):

    def __init__(self):
        self.stack, self.min = [], []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min or val < self.min[-1][0]:
            self.min.append((val, len(self.stack)))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) < self.min[-1][1]:
          self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1][0]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
