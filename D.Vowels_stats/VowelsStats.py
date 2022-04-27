string1 = input()
list1 = list("ueoai")
list1_num = []
list1_char = []

for index in range(len(list1)):
    n = string1.count(list1[index])
    if n == 0:
        continue
    list1_num.append(n)
    list1_char.append(list1[index])

for index in range(len(list1_num) - 1):
    for index1 in range(len(list1_num) - index - 1):
        if list1_num[index1] > list1_num[index1 + 1]:
            list1_num[index1], list1_num[index1 + 1] = (
                list1_num[index1 + 1],
                list1_num[index1],
            )
            list1_char[index1], list1_char[index1 + 1] = (
                list1_char[index1 + 1],
                list1_char[index1],
            )
        if list1_num[index1] == list1_num[index1 + 1]:
            if list1_char[index1] > list1_char[index1 + 1]:
                list1_char[index1], list1_char[index1 + 1] = (
                    list1_char[index1 + 1],
                    list1_char[index1],
                )
                list1_num[index1], list1_num[index1 + 1] = (
                    list1_num[index1 + 1],
                    list1_num[index1],
                )

for index in range(len(list1_num)):
    string = list1_char[index] + "(" + str(list1_num[index]) + ")"
    print(string)
