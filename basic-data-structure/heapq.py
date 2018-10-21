h=[]                    #定义一个list
from heapq import *     #引入heapq模块
h
# []
heappush(h,5)               #向堆中依次增加数值
heappush(h,2)
heappush(h,3)
heappush(h,9)
h                           #h的值
# [2, 5, 3, 9]
heappop(h)                  #从h中删除最小的，并返回该值
# 2
h
# [3, 5, 9]
h.append(1)                 #注意，如果不是压入堆中，而是通过append追加一个数值
h                           #堆的函数并不能操作这个增加的数值，或者说它堆对来讲是不存在的
# [3, 5, 9, 1]
heappop(h)                  #从h中能够找到的最小值是3,而不是1
# 3
heappush(h,2)               #这时，不仅将2压入到堆内，而且1也进入了堆。
h
# [1, 2, 9, 5]
heappop(h)                  #操作对象已经包含了1
# 1

h
# [1, 2, 9, 5]
heappop(h)
# 1
heappushpop(h,4)            #增加4同时删除最小值2并返回该最小值，与下列操作等同：
# 2                               #heappush(h,4),heappop(h)
h
# [4, 5, 9]

a = [4, 5, 9, 6]
heapreplace(a,1)            #1是后来加入的，在1加入之前，a中的最小值是4
# 4
a
# [1, 5, 9, 6]