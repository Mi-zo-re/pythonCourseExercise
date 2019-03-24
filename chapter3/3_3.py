L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [mem.lower() for mem in L1 if isinstance(mem, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')