list_of_num = []
num = 1
while num < 101:
    list_of_num.append(num)
    current_num = num
    for row in range(num - 1):
        current_num +=num
        list_of_num.append(current_num)

    print(list_of_num)
    num += 1
    list_of_num = []