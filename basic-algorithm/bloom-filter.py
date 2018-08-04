import mmh3
from bitarray import bitarray

BIT_SIZE = 5000000


class BloomFilter(object):
    def __init__(self):
        self.bit_array = bitarray(BIT_SIZE)
        self.bit_array.setall(0)

    def add(self, addr):
        point_list = self.get_positions(addr)
        for b in point_list:
            self.bit_array[b] = 1

    def contains(self, addr):
        point_list = self.get_positions(addr)

        result = True
        for b in point_list:
            result = result and self.bit_array[b]

        return result

    def get_positions(self, addr):
        # Get points positions in segment tree vector.
        point1 = mmh3.hash(addr, 41) % BIT_SIZE
        point2 = mmh3.hash(addr, 42) % BIT_SIZE
        point3 = mmh3.hash(addr, 43) % BIT_SIZE
        point4 = mmh3.hash(addr, 44) % BIT_SIZE
        point5 = mmh3.hash(addr, 45) % BIT_SIZE
        point6 = mmh3.hash(addr, 46) % BIT_SIZE
        point7 = mmh3.hash(addr, 47) % BIT_SIZE

        return [point1, point2, point3, point4, point5, point6, point7]

bloom = BloomFilter()
bloom.add("0x10102345")
bloom.add("0x23432342")
bloom.add("0x23435254")
print(bloom.contains("0x10102344"))
