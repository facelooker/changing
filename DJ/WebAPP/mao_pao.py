a=[1,5,8,2,10,9,21,7,7]

len_num = len(a)
for i in range(len_num):#外循环为最多的循环次数
    sort_sign = False
    for j in range(len_num - 1 - i): #内循环为最对的比较次数
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            sort_sign =True

    if not sort_sign:
        break
print(a)