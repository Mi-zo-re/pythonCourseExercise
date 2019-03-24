def mov(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        mov(n-1, a, c, b)
        print(a, '--->', c)
        mov(n-1, b, a, c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
mov(3, 'A', 'B', 'C')