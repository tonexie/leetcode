from collections import deque


def subsets(nums):
    queue = deque([[]])
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr)
        for num in nums:
            if not curr or num > curr[-1]:
                sub = curr + [num]
                queue.append(sub)
    return res

print(subsets([1, 2, 3]))
