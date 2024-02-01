import heapq

def maxSlidingWindow(nums, k: int):
    result = []
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k-1:
            (val, index) = heap[0]
            print(val, index)
            while heap and index <= i - k:
                heapq.heappop(heap)
                (val, index) = heap[0]
            result.append(-val)
    return result


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
