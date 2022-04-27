while True:
    n = int(input())
    if 1 <= n <= 100:
        break

list_tmp = []
list_out = []
for index in range(n):
    list1 = list(map(int, input().split()))
    list_tmp.append(list1)

for index in range(n):
    flag = True
    for index1 in range(n):
        if list_tmp[index][index1] != 0:
            flag = False
            break
    if flag:
        list_out.append(index)

string = ""
if len(list_out) != 0:
    for index in range(len(list_out)):
        string += str(list_out[index]) + ","
    print(string.rstrip(","))
else:
    print("None")
