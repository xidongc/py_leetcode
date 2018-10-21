#
# Complete the 'usernamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY u as parameter.
#
# import collections
def usernamesSystem(u):
    #
    # countDict = collections.Counter(u)
    # Create a count list
    countDict = {name:0 for name in u}
    for i in range(len(u)):
        name = u[i]
        if countDict[name] > 0:
            u[i] = name + str(countDict[name])
        countDict[name] += 1
    return u






    # [alex,xylos,alex,alan] ->     alex, xylos,alex1,    alan
