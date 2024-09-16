def subsets1(nums):
    list = []
    nums.sort()
    backtrack1(list, [], nums, 0)
    return list


def backtrack1(list, tempList, nums, start):
    list.append(tempList[:])
    for i in range(start, len(nums)):
        tempList.append(nums[i])
        backtrack1(list, tempList, nums, i + 1)
        tempList.pop()


print(subsets1([1, 2, 3]))
