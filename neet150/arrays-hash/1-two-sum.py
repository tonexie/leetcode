# my solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for i in range(len(nums)):
            # this accounts for duplicate keys
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)

        for j in hashmap:
            index = hashmap[j]
            diff = target - j
            if diff in hashmap:
                # handles case where sum is duplicate
                if len(hashmap[diff]) > 1:
                    return index
                # ensures that not using same element twice
                elif index != hashmap[diff]:
                    return [index[0], hashmap[diff][0]]

# my neetcode
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        
        # incrementally add to the hashmap
        for i in range(len(nums)):
          num = nums[i]
          diff = target - num
          if diff in hashmap:
            return [hashmap[diff], i]
          hashmap[num] = i



solution = Solution()

nums = [3, 3]
target = 6

print(solution.twoSum(nums, target))
