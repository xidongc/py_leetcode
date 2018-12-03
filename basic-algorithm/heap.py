from collections import OrderedDict

class SmallHeap(object):

    def __init__(self, max_size=-1, hash_heap = False):
        self.heap_array = [0]
        self.current_size = 0
        self.max_size = max_size
        self.hash_heap = hash_heap

        if hash_heap:
            self.hash_dic = OrderedDict()

    def heapify(self, array):
        for ele in array:
            self.insert(ele)

    def insert(self, x):
        self.heap_array.append(x)
        self.current_size += 1
        l = self.current_size
        self._up(l)

    def sort(self):
        ret = []
        while True:
            tmp = self._down()
            if tmp is None:
                break
            else:
                ret.append(tmp)
        print(ret)
        return ret

    def pop(self):
        return self._down()

    def _up(self, i):
        # it has parent
        ROOT_index = 1
        val = self.heap_array[i]

        while i//2 >= ROOT_index:
            if self.heap_array[i//2] > self.heap_array[i]:
                self.heap_array[i] = self.heap_array[i//2]
                i = i//2
            else:
                break
        self.heap_array[i] = val

    def _down(self):
        if self.current_size < 1:
            print("current heap array empty! ")
            return None
        ret = self.heap_array[1]

        sub = self.heap_array[self.current_size]
        self.heap_array.pop(1)
        self.heap_array.insert(1, sub)
        self.heap_array.pop(-1)
        self.current_size -= 1

        start = 1
        while start * 2 < self.current_size:
            if self.heap_array[start] > min(self.heap_array[2*start], self.heap_array[2*start+1]):
                if self.heap_array[2*start] <= self.heap_array[2*start+1]:
                    self.heap_array[start], self.heap_array[2*start] = self.heap_array[2*start], self.heap_array[start]
                    start = 2*start
                else:
                    self.heap_array[start], self.heap_array[2*start+1] = self.heap_array[2*start+1], self.heap_array[start]
                    start = 2*start + 1
            else:
                break
        if start*2 == self.current_size and self.heap_array[start*2] < self.heap_array[start]:
            self.heap_array[start], self.heap_array[2 * start] = self.heap_array[2 * start], self.heap_array[start]
        return ret

h = SmallHeap()
h.heapify([1,4,3,5,2,7,6,9,5])
print(h.heap_array)

h.sort()





