class Sort(object):

    def merge_sort(self, array):

        # average O(nlgn)
        # worst O(nlgn)
        # stable sort

        if len(array) <= 1:
            return array

        def _merge(array1, array2):
            # assume array1 and array2 are not empty
            tmp = []
            p1 = p2 = 0
            while p1 < len(array1) and p2 < len(array2):
                if array1[p1] <= array2[p2]:
                    tmp.append(array1[p1])
                    p1 += 1
                else:
                    tmp.append(array2[p2])
                    p2 += 1
            if p1 == len(array1):
                tmp.extend(array2[p2:])
            elif p2 == len(array2):
                tmp.extend(array1[p1:])
            return tmp

        mid = len(array) // 2
        array1 = self.merge_sort(array[0:mid])
        array2 = self.merge_sort(array[mid:])
        return _merge(array1, array2)

    def quick_sort(self, array, l, r):
        def partition(array, l, r):
            cmp = array[r]
            p1 = l
            p2 = l
            while p2 < r:
                if array[p2] <= cmp:
                    array[p1], array[p2] = array[p2], array[p1]
                    p1 += 1
                p2 += 1
            array[p1], array[r] = array[r], array[p1]
            return p1
        if l < r:
            q = partition(array, l, r)
            self.quick_sort(array, l, q - 1)
            self.quick_sort(array, q + 1, r)
        return array

    def quick_sort_2(self, array, left_index, right_index):
        if left_index > right_index:
            return

        cmp = array[left_index]
        p1 = p2 = left_index+1
        while p2 <= right_index:
            if array[p2] <= cmp:
                array[p1], array[p2] = array[p2], array[p1]
                p1 += 1
            p2 += 1
        array[p1-1], array[left_index] = array[left_index], array[p1-1]
        self.quick_sort(array, left_index, p1-2)
        self.quick_sort(array, p1, right_index)
        return array




s = Sort()
test = [2,5,4,1,7,5,6,9,8]
