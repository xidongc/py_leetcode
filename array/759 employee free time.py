#yelp
from itertools import chain
def employeeFreeTime(self, avails):
    timeList = sorted(chain(*avails),key=lambda interval:interval.start)
    # 排序后interval只剩下三种关系
    # 包含，overlap，不overlap
    begin, end = timeList[0].start,timeList[0].end
    res = []
    for i in range(1,len(timeList)):
        if timeList[i].start > end:
            res.append([end,timeList[i].start])
            begin, end = timeList[i].start, timeList[i].end
        elif timeList[i].end > end:
            end = timeList[i].end
    return res
# [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
