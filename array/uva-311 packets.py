#
# def getParcelNumber():
#     """
#     :param matrix: list[list[string]]
#     :return: list[list[int]]
#     """
import sys
import math
for line in sys.stdin:
# line = "5000 1400 300 200 100 100"
# line = "39 33 94 31 7 55"
    order = list(map(int, line.split(" ")))
    # print(order)
    if not order[0] and not order[1] and not order[2] and not order[3] and not order[4] and not order[5]:
        break
    # size 4,5,6
    tmpRes = order[5] + order[4] + order[3]

    #     size 3
    tmpRes += int(math.ceil(order[2] / 4))
    order[2] = order[2] % 4
    #     size1 and size2 with size3
    order[0] -= order[4] * 11
    order[1] -= order[3] * 5
    if order[2] == 1:
        order[1] -= 5
        order[0] -= 7
    elif order[2] == 2:
        order[1] -= 3
        order[0] -= 6
    elif order[2] == 3:
        order[1] -= 1
        order[0] -= 5
    if order[1] > 0:
        tmpRes += int(math.ceil(order[1] / 9))
        # 减去number of box of size 2, including 没填满的最后一个box
        order[1] -= 9 * int(math.ceil(order[1] / 9))
    if order[1] < 0:
        order[0] += order[1] * 4
    if order[0] > 0:
        tmpRes += int(math.ceil(order[0] / 36))
    print(tmpRes)
        # res.append(tmpRes)
        # print(res)
# print(getParcelNumber([["0 0 4 0 0 1"],["7 5 1 0 0 0"],["0 0 0 0 0 0"]]))





