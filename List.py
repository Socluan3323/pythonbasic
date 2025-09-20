list = [1,2,3,4,5,6,5,7,8,9]
# list.insert(3,4)
# list.append(10)
# list.pop(1)
# for i in range(len(list)-1,-1,-1):
    # if list[i] == 5:
        # del list[i]
    # print(list[i])
# del list[1]
for i in range(len(list)-1,-1,-1):
    if list[i] == 5:
        list.remove(5)
print(list)
