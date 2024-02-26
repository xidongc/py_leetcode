import heapq


class Ele:
    def __init__(self, word, val):
        self.word = word
        self.val = val

    def __lt__(self, other) -> bool:
        if self.val < other.val:
            return True
        elif self.val == other.val:
            return self.word > other.word
        return False


class Solution:
    # Sol-1 using min heap to get top-k
    # TP: O(log(k) * n), SP: O(n)
    def topKFrequent(self, words, k: int):
        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1

        heap = []
        i = 0
        for key, val in hashmap.items():
            if i < k:
                heapq.heappush(heap, Ele(key, val))
            else:
                heapq.heappush(heap, Ele(key, val))
                heapq.heappop(heap)
            i += 1
        heap.sort(reverse=True)
        arr = [ele.word for ele in heap]
        return arr

    # Sol-2 using quick select
    # TP: O(n) - O(n*n), SP: O(n)
    def topKFrequent_2(self, words, k: int):
        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1
        print(hashmap)
        arr = [Ele(key, val) for key, val in hashmap.items()]
        results = self.quick_select(arr, k - 1, 0, len(arr) - 1)
        results.sort(reverse=True)
        return [result.word for result in results]

    def quick_select(self, arr, k, start, end):
        # (key, val)
        pivot = arr[start]
        i, j = start, end
        while i <= j:
            while i <= j and arr[i] > pivot:
                i += 1
            while i <= j and arr[j] < pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if k <= j:
            return self.quick_select(arr, k, start, j)
        elif k >= i:
            return self.quick_select(arr, k, i, end)
        return arr[:k + 1]
