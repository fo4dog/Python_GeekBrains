list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
print(list1)
print(list2)