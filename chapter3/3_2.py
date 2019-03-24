def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    minNum = L[0]
    maxNum = L[0]
    for num in L:
        if num < minNum:
            minNum = num
        if num > maxNum:
            maxNum = num
    return (minNum, maxNum)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')