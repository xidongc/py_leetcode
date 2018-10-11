#
# Complete the 'countHoles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER num as parameter.
#

def countHoles(num):
    pathMap = {1:0,2:0,3:0,5:0,7:0,0:1,4:1,6:1,9:1,8:2}
    numStr = list(map(int,str(num)))
    res = 0
    for number in numStr:
        res += pathMap[number]
    return res
