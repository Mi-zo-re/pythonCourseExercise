def trim(s):
    if s == '':
        return s
    else:
        r1 = 0
        while s[r1] == ' ':
            r1 = r1 + 1
            if r1 == len(s):
                return ''
        r2 = -1
        while s[r2] == ' ':
            r2 = r2 - 1
        if r2 == -1:
            return s[r1:]
        else:
            r2 = r2 + 1
            return s[r1:r2]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')