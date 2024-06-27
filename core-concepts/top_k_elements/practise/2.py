import heapq

# Given an array of integers and an integer K, find the K largest elements.
array = [3, 1, 5, 12, 2, 11, 7, 6, 4, 8]
k = 3

def topKElements(array, k):
  minHeap = array[:k]
  heapq.heapify(minHeap)
  
  for n in array[k:]:
    if n > minHeap[0]:
      heapq.heappop(minHeap)
      heapq.heappush(minHeap, n)
      
  return minHeap

print(topKElements(array, k))