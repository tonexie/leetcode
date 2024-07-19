import heapq


class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        if not self.leftHeap:
            heapq.heappush(self.leftHeap, num * -1)
        elif num > self.leftHeap[0] * -1:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, num * -1)

        leftLen = len(self.leftHeap)
        rightLen = len(self.rightHeap)

        if leftLen - rightLen > 1:
            temp = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, temp * -1)
        elif rightLen - leftLen > 1:
            temp = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, temp * -1)

    def findMedian(self) -> float:
        leftLen = len(self.leftHeap)
        rightLen = len(self.rightHeap)
        if leftLen > rightLen:
            return float(self.leftHeap[0] * -1)
        elif rightLen > leftLen:
            return float(self.rightHeap[0])
        else:
            return (self.leftHeap[0] * -1 + self.rightHeap[0]) / 2

        # self.dataList.sort()
        # if len(self.dataList) % 2 == 1:
        #     return float(self.dataList[len(self.dataList) // 2])
        # else:
        #     leftInd = len(self.dataList) // 2 - 1
        #     return (self.dataList[leftInd] + self.dataList[leftInd + 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
