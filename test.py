list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in list1[:]:
    if i in list2:
        list1.remove(i)
print(list1)
print(list2)