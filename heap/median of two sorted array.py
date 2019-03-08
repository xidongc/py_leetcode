import heapq


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # use heap
        m = len(nums1)
        n = len(nums2)

        if m == 0 and n == 0:
            return 0
        elif m == 0:
            if n % 2 == 0:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
            else:
                return nums2[n // 2]
        elif n == 0:
            if m % 2 == 0:
                return (nums1[m // 2 - 1] + nums1[m // 2]) / 2
            else:
                return nums1[m // 2]

        target1_index = (m + n - 1) // 2
        target2_index = (m + n - 1) // 2 + 1
        target1 = 0
        target2 = 0

        current_index = -1

        heap = list()
        heapq.heapify(heap)
        heapq.heappush(heap, (nums1[0], 1, 0))
        heapq.heappush(heap, (nums2[0], 2, 0))

        while len(heap) > 0:
            current_index += 1

            ele = heapq.heappop(heap)

            if current_index == target1_index:
                target1 = ele[0]

            elif current_index == target2_index:
                if (m + n) % 2 == 0:
                    target2 = ele[0]
                else:
                    target2 = target1

            if ele[1] == 1 and ele[2] < m - 1:
                heapq.heappush(heap, (nums1[ele[2] + 1], 1, ele[2] + 1))
            elif ele[1] == 2 and ele[2] < n - 1:
                heapq.heappush(heap, (nums2[ele[2] + 1], 2, ele[2] + 1))

        print(target1, target2)
        return (target1 + target2) / 2