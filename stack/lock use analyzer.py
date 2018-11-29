# Complete the check_log_history function below.
def check_log_history(events):
    stack = []
    row = 0
    for event in events:
        row += 1
        if event.startswith('A'):
            lockNum = event.split(' ')[1]
            # 重复输入
            if lockNum in stack:
                return row
            stack.append(lockNum)
        else:
            lockNum = event.split(' ')[1]
            if stack.pop() != lockNum:
                return row
    #         检查栈空
    return 0 if not stack else row + 1
# 各种边界条件

# 正解
# 1. ACQUIRE 364
# 2. ACQUIRE 84
# 3. RELEASE 84
# 4. RELEASE 364

# 错误
# 1. ACQUIRE 364
# 2. ACQUIRE 84
# 3. RELEASE 84
# 4. ACQUIRE 364
# 5. RELEASE 364

# 错误
# 1. ACQUIRE 364
# 2. ACQUIRE 84
# 3. RELEASE 364
# 4. RELEASE 84

# 错误
# 1. ACQUIRE 364
# 2. ACQUIRE 84
# 3. RELEASE 84
# 4. ACQUIRE 87 什么都没做就直接退出了

# ACQUIRE OR RELEASE NON EXIST, AGAIN

