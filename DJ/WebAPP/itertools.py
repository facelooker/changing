import json
from itertools import combinations
import yaml



a=[-2,3,5,0,-1,2,1]
aa=()
# print(type(new_turple))
new_list = []
for i in list(combinations(a,3)):
    i = list(i)
    if i[0]+i[1]+i[2] == 0:
        for j in range(len(i)):
            sort_sign = False
            for z in range(len(i) - 1 - j):
                if i[z] > i[z+1]:
                    i[z],i[z+1] = i[z+1],i[z]
                    sort_sign =True
            if not sort_sign:
                break
        if i[2] != 3:
            new_list.append(i)

aa = tuple(new_list)
# print(aa)

"""
每走3步 剩下2个阶梯
每走4步 剩下3个阶梯
每走5步 剩下4个阶梯
每走6步 剩下5个阶梯
每走7步 正好没剩。
求结果：
有多少个阶梯？

i = 阶梯数
step = 步数
"""
i = 0
step = 0
while step !=1:
    i = i+1
    if (i - 2) % 3 ==0:
        if(i - 3)%4 ==0:
            if (i -4)%5 ==0:
                if(i -5)%6==0:
                    if(i%7)==0:
                        step =1

# print(i)
"""
递归阶乘
9*8*7*6....
"""

def fuc(n):
    if n <=1:
        return 1
    else:
        return n*fuc(n-1)

# print(fuc(4))


"""
 {"a":"0","b":"1","d":"11","e":"22","f":"33"}, 
"""
json_str = '{"a":"0","b":"1","d":"11","e":"22","f":"33"}'
json_dict = json.loads(json_str)
# print(json_dict)


"""
             fin one  : 13700010001 15 52A
             fin two  : 13700020002 15 52B
             fin three : 13700030003 15 52C
   依次代表 姓名 ：手机号   楼栋号  房间号
   请输出
   姓名 ：...，电话：...........，住址：......
   姓名 ：...，电话：...........，住址：......
   姓名 ：...，电话：...........，住址：......
"""
# str1 = 'fin one  : 13700010001 15 52A'
# str1_list = str1.split(":")
# print(str1_list)
# str1_list[1].strip()
# str1_list_2 = str1_list[1].split(" ")
# print(str1_list_2)


ss="abcdefgh"
ss_e = ss.index("e")
ss_new = ss[0:ss_e+1]
# print(ss_new)

"""
对字符串“www.autotestplat.com"，输出为“com.autotestplat.www"
"""

domain = "www.autotestplat.com"
domain = list(domain.split("."))
domain.reverse()
print('.'.join(domain))