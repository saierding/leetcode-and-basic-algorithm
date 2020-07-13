test = [9, 15, 27, 35, 6]


dict1, dict2 = {}, {}
for i in range(0, 50):
    dict1[i*2+1] = i
    dict2[(i+1)*2] = i

for i in test:
    if i in dict1:
        dict1.pop(i)
    if i in dict2:
        dict2.pop(i)

list1 = list(dict1.values())
list2 = list(dict2.values())
best2 = 0
best1 = 0
for x in list1:
    if x - 1 not in list1:
        y = x + 1
        while y in list1:
            y += 1
        best1 = max(best1, y - x)
for x in list2:
    if x - 1 not in list2:
        y = x + 1
        while y in list2:
            y += 1
        best2 = max(best2, y - x)


print(max(best1, best2))

