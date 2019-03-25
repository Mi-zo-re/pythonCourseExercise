import time, functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        before = time.time()
        result = func(*args, **kw)
        after = time.time()
        print('%s excuted in %s ms'% (func.__name__, after - before))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')