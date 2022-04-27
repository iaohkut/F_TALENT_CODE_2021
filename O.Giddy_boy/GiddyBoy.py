while True:
    x, y = map(int, input().split())
    if (-10) ** 9 <= x <= (10) ** 9 and (-10) ** 9 <= y <= (10) ** 9:
        break

while True:
    string1 = input().upper()
    if len(string1) <= 1000:
        break

list1 = list("NSWE")
list1_num = []
list1_char = []
for index in range(len(list1)):
    n = string1.count(list1[index])
    if n == 0:
        continue
    list1_num.append(n)
    list1_char.append(list1[index])
for index in range(len(list1_num)):
    if list1_char[index] == "N":
        y += list1_num[index]
    if list1_char[index] == "S":
        y -= list1_num[index]
    if list1_char[index] == "W":
        x -= list1_num[index]
    if list1_char[index] == "E":
        x += list1_num[index]

print("(", x, ",", y, ")", sep="")
