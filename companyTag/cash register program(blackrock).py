# Programming Challenge Description:
# The goal of this challenge is to design a cash register program. You will be given two decimal numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your register currently has the following bills/coins within it:
# 'PENNY': .01,
# 'NICKEL': .05,
# 'DIME': .10,
# 'QUARTER': .25,
# 'HALF DOLLAR': .50,
# 'ONE': 1.00,
# 'TWO': 2.00,
# 'FIVE': 5.00,
# 'TEN': 10.00,
# 'TWENTY': 20.00,
# 'FIFTY': 50.00,
# 'ONE HUNDRED': 100.00
# The aim of the program is to calculate the change that has to be returned to the customer.
# Input:
# Your program should read lines of text from standard input. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price (PP) and the second is the cash(CH) given by the customer.
# Output:
# For each line of input print a single line to standard output which is the change to be returned to the customer. In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned, in terms of the currency values provided. The output should be alphabetically sorted.
# -*- coding: utf-8 -*-

# test case1
# 15.94;16.00
# NICKEL,PENNY

# test case2
# 17;16
# ERROR

# test case3
# 35;35
# ZERO

# test case4
# 45;50
# FIVE
import sys
import bisect
changeDict = {0.01:'PENNY',0.05:'NICKEL', 0.10:'DIME', 0.25:'QUARTER', 0.50:'HALF DOLLAR',1.00:'ONE',2.00:'TWO',5.00:'FIVE',10.00:'TEN',20.00:'TWENTY',50.00:'FIFTY',100.00:'ONE HUNDRED'}

for line in sys.stdin:
# line = '17;16'
    pp,ch = line.split(';')
    pp,ch = float(pp),float(ch)
    if ch < pp:
        print('ERROR')
    elif ch == pp:
        print('ZERO')
    else:
        res = ''
        # 为什么float相减之后多出来很多位
        change = round(ch - pp,2)
        keyList = list(changeDict.keys())
        while change > 0:
            pos = bisect.bisect(keyList, change) - 1
            res += changeDict[keyList[pos]] + ','
            change = round(change % keyList[pos],2)
        print(res[:-1])


