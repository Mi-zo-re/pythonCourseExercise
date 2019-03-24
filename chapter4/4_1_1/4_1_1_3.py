from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2,
'3': 3, '4': 4, '5': 5,
'6': 6, '7': 7, '8': 8,
'9': 9}

def char2num(s):
    return DIGITS[s]

def func1(x, y):
    return x * 10 + y

def func2(x, y):
    return x * 0.1 + y

def str2float(s):
    point = s.index('.')
    s1 = s[0: point]
    s2 = s[point+1:]
    s2 = s2[::-1]
    n1 = reduce(func1, map(char2num, s1))
    n2 = reduce(func2, map(char2num, s2))
    return n1 + n2 * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')