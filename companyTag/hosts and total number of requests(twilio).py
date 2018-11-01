import collections
countDict = collections.defaultdict(int)
filename = input()
with open(filename, 'rt') as f:
    for line in f:
        hostname = line.split(' ')[0]
        countDict[hostname] += 1
with open('records_' + filename, 'wt') as f:
    for key,value in countDict.items():
        print(key + ' ' + str(value), file=f)
    # 就是给输入记数
    # 输入:
    # unicorn.com - - [hb;joijhliygbi;]h;iuhu;
    # google.com - -[efwrafe] GETHU;JOJ;OJJ;O