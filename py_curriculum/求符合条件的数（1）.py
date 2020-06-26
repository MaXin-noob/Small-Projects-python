s = list()
for i in range(1000, 10000):
    d = int(i / 1 % 10)
    c = int(i / 10 % 10)
    b = int(i / 100 % 10)
    a = int(i / 1000 % 10)
    m1 = a * 10 + b
    m2 = c * 10 + d
    m3 = m1 + m2
    m4 = m3 ** 2
    if m4 == i:
        print("因为%d分解后为%d，%d，%d，%d" % (i, a, b, c, d))
        print("而 %d + %d 的平方恰好等于 %d" % (m1, m2, i))
        print("所以%d符合要求" % i)
        s.append(i)
else:
    print("满足第一题要求的数如下：")
    print(s)
