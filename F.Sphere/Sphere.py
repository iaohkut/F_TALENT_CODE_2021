while True:
    d = int(input())
    if 0 < d < (10 ** 9):
        break

pi = 3.1415926

r = d / 2

V = (4 / 3) * pi * (r ** 3)
A = pi * (d ** 2)

print("%.3f %.3f" % (V, A))
