while True:
    n = int(input())
    if 0 <= n < 63:
        break
k2 = 0

for index in range(n + 1):
    k2 += 2 ** index
k1 = 2 ** n

print(k1, k2)
