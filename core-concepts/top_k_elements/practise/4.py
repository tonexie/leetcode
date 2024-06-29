import heapq
# Given an array of integers and an integer K, find the K largest elements.
array = [3, 1, 5, 12, 2, 11, 7, 6, 4, 8]
k = 6

def topK(arr, k):
  minHeap = arr[:k]
  heapq.heapify(minHeap)
  
  for n in arr[k:]:
    if n > minHeap[0]:
      heapq.heappop(minHeap)
      heapq.heappush(minHeap, n)
      
  return minHeap

print(topK(array, k))