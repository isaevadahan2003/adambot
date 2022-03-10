numbers = [2, 7, 11, 15]
goal = 9
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) == goal:
            print(i, j)

list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]


print(list1)
print(list2)
print(list3)

list = [list1, list2, list3]
for list in list:
    list.extend(list)

list1.extend(list1)
list2.extend(list2)
list3.extend(list3)

print(f'{list1}\n{list2}\n{list3}')


