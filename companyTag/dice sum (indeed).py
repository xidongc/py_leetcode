# 写一个函数float sumPossibility(int dice, int target)，就是投dice个骰子，求最后和为target的概率。
# brute force = combination sum
# 记忆化搜索

def getPossibilities(dice,target):
    if dice < 0 or target < dice:
        return 0
    memo = [[0 for i in range(target+1)] for j in range(dice+1)]
    def dfs(dice, target, memo):
        count = 0
        if dice == 0 and target == 0:
            return 1
        if target > dice * 6 or target < dice:
            return 0
        if memo[dice][target] != 0:
            return memo[dice][target]
        for i in range(1, 7):
            count += dfs(dice-1,target-i,memo)
        memo[dice][target] = count
        return count
    count = dfs(dice,target,memo)
    print(memo)
    print(count)
    return float(count) / float((6 ** dice))

print(getPossibilities(3,12))


