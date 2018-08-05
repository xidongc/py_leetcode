from bitarray import bitarray

BIT_SIZE = 500


class Clock(object):

    def __init__(self):
        self.page_in_block = None  # key value pair
        self.bit_array = bitarray(BIT_SIZE)
        self.bit_array.setall(0)

    def clock(self, index):
        if self.page_in_block[index]:
            self.bit_array[index] = 1
        else:
            while True:
                # find self.bit_array = 0



