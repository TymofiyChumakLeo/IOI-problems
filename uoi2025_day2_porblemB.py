n, m = map(int, input().split())
def n1(m):
    res = []
    cnt = 0
    if m % 3 == 0:
        for _ in range(m):
            if cnt % 3 == 0:
                res.append('0')
                cnt += 1
            else:
                res.append('1')
                cnt += 1
    if m % 3 == 2:
        for _ in range(m):
            if cnt % 3 == 2:
                res.append('0')
                cnt += 1
            else:
                res.append('1')
                cnt += 1
    if m % 3 == 1:
        for _ in range(m):
            if cnt % 3 == 0:
                res.append('0')
                cnt += 1
            else:
                res.append('1')
                cnt += 1
    print(*res)
def n2(m):
    n1 = []
    cnt = 0
    if m % 3 == 0:
        for _ in range(m):
            if cnt % 3 == 0:
                n1.append('1')
                cnt += 1
            else:
                n1.append('2')
                cnt += 1
    if m % 3 == 2:
        for _ in range(m):
            if cnt % 3 == 2:
                n1.append('1')
                cnt += 1
            else:
                n1.append('2')
                cnt += 1
    if m % 3 == 1:
        for _ in range(m):
            if cnt % 3 == 0:
                n1.append('1')
                cnt += 1
            else:
                n1.append('2')
                cnt += 1
    n2 = n1.copy()
    print(*n1)


if n == 1:
    n1(m)

elif n == 2:
    n2(m)
    n2(m)
elif n == 3:
    n1(m)
    n2(m)
    n2(m)

else:
    if n % 3 == 2:
        for i in range(n):
            if i % 3 == 2:
                n1(m)
            else:
                n2(m)
        
    else:
        for i in range(n):
            if i % 3 == 0:
                n1(m)
            else:
                n2(m)

    