x, n = map(int, input().split())

if 1 <= x <= pow(10, 6) and 1 <= n <= pow(10, 2):
    sum = 0
    for i in range(1, n + 1):
        tmp = 1
        for i in range(1, i + 1):
            tmp *= i
        sum += int(tmp / x)

    print(x + sum)
