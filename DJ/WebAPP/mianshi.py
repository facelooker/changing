# a=1
# b=2
# a = a ^ b
# b = a ^ b
# a = a ^ b
#
# print(a)
# print(b)
# name_list = ['a','b','c']
#
# if 'g' in name_list:
#     print('sss')
# else:
#     name_list.append('sss')
# print(name_list)

# my_list = ['P','y','t','h','o','n']
# print(sorted(my_list))
# print(my_list)
# print(sorted(my_list,reverse=True))

# a=4%4
# print(a)
# num=1234
# num3=str(num)
# num2 = []
# for i in num3:
#     i=int(i)
#     i=(i+3)%9
#     # print(type(i))
#     num2.append(int(i))
# # print(num2)
# for i in num2:
#      print(i,end='')
# # print(num4)
import re

num_list = [1,2,3,4]
# num_list.pop()
# num_list[0],num_list[2] = num_list[2],num_list[0]
# num_list[1],num_list[3] = num_list[3],num_list[1]

# for i in range(3):
#     print(i)
# print(num_list)

# group_list=[ 'Tom', 'Allen', 'Jane', 'William', 'Tony' ]
#
# print(group_list[0:2])
# print(group_list[1:4])
# print(group_list[3:5])

#
new_users = ['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
current_users = ['Niuniu','Niumei','GURR','LOLO']

user_not_in_cur = ''
user_in_cur = ''
for i in new_users:
    for y in current_users:
        if i.lower() == y.lower():
            print("The user name {} has already been registered! Please change it and try again!".format(i))
            user_in_cur = i
            break
        else:
            user_not_in_cur = i

    if user_not_in_cur != user_in_cur:
        print("Congratulations, the user name {} is available!".format(user_not_in_cur))