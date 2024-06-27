from collections import deque

def subsets(nums):
    result = []
    queue = deque([[]])  # Initialize the queue with an empty subset
    
    while queue:
        current_subset = queue.popleft()  # Get the first subset in the queue
        result.append(current_subset)  # Add it to the result list
        
        # Generate new subsets by adding each element of nums not yet in current_subset
        for num in nums:
            if not current_subset or num > current_subset[-1]:  # Ensure new elements are in increasing order to avoid duplicates
                new_subset = current_subset + [num]  # Create a new subset including num
                queue.append(new_subset)  # Add the new subset to the queue
    
    return result

# Example usage
nums = [1, 2, 3]
print(subsets(nums))


# def subsets(nums):
#     result = []
#     subset = []
    
#     def backtrack(start):
#         result.append(subset.copy())
        
#         for i in range(start, len(nums)):
#             subset.append(nums[i])
#             backtrack(i + 1)
#             subset.pop()
    
#     backtrack(0)
#     return result

# # Example usage
# nums = [1, 2, 3]
# print(subsets(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
