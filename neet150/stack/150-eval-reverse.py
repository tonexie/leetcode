class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack = []
        output = 0
        firstDigit = True
        operators = ["+", "-", "*", "/"]
        if len(tokens) == 1:
            return int(tokens[0])

        for  t in tokens:
            if firstDigit and t in operators:
                firstDigit = False
                num = numStack.pop()
                output += num
            if t == "+":
                num = numStack.pop()
                output = num + output
            elif t == "-":
                num = numStack.pop()
                output =   num - output
            elif t == "*":
                num = numStack.pop()
                output = num * output
            elif t == "/":
                num = numStack.pop()
                output = int(num / output)
            else:
                t = int(t)
                numStack.append(t)
            print(numStack)

        return output


# class Solution:
#     def evalRPN(self, tokens):
#         stack = []
#         for c in tokens:
#             if c == "+":
#                 stack.append(stack.pop() + stack.pop())
#             elif c == "-":
#                 a, b = stack.pop(), stack.pop()
#                 print(a)
#                 print(b)
#                 stack.append(b - a)
#             elif c == "*":
#                 stack.append(stack.pop() * stack.pop())
#             elif c == "/":
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(int(float(b) / a))
#             else:
#                 stack.append(int(c))
#             print(stack)
            
#         return stack[0]

sol = Solution()
tokens = ["3","11","+","5","6","-", "-"]
print(sol.evalRPN(tokens))
# print(int(round(float(13)/5)))
# print(13//5)
