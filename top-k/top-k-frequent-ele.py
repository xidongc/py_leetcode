import heapq


class Solution:

    # Sol-1 using min heap to get top-k
    # TP: O(log(k) * n), SP: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        i = 0
        for key, val in hashmap.items():
            if i < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
                heapq.heappop(heap)
            i += 1
        heap.sort(reverse=True)
        return [h[1] for h in heap]

    # Sol-2 using quick select
    # TP: O(n) - O(n*n), SP: O(n)
    def topKFrequent_2(self, nums, k: int):
        def quick_select(nums, start, end, k):
            pivot = nums[start][1]
            i, j = start, end
            while i <= j:
                while i <= j and nums[i][1] > pivot:
                    i += 1
                while i <= j and nums[j][1] < pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            if k <= j:
                quick_select(nums, start, j, k)
            elif k >= i:
                quick_select(nums, i, end, k)
            return nums[:k+1]

        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        arr = [(key, val) for key, val in hashmap.items()]
        results = quick_select(arr, 0, len(arr)-1, k-1)
        return [result[0] for result in results]
