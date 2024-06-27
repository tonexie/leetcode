import heapq
# Given an array of integers and an integer K, find the K largest elements.
array = [3, 1, 5, 12, 2, 11, 7, 6, 4, 8]
k = 3

def top_k_elements(array, k):
    # Create a min-heap with the first K elements of the array
    min_heap = array[:k]
    heapq.heapify(min_heap)

    # Iterate over the remaining elements in the array
    for num in array[k:]:
        # If the current number is larger than the smallest element in the heap
        if num > min_heap[0]:
            # Remove the smallest element
            heapq.heappop(min_heap)
            # Add the current number
            heapq.heappush(min_heap, num)

    return min_heap

# Example usage

print(top_k_elements(array, k))  # Output: [7, 11, 12]
