class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                temp = stack.pop()
                output[temp[0]] = i - temp[0]
            stack.append((i, t))
                    
        return output


sol = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.dailyTemperatures(temperatures))
