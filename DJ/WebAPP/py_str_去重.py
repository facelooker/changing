"""
去重后输出首字符
全部重复，则输出""或None
输出首字符，区分大小写
"""
str = 'sTress'
str_ss = 'ssssss'

def solution(string,exp):
    string = string.strip()
    str2 = list(set(string))
    # print(type(str2))
    if str2.__len__() ==1:
       print("sss")
       return str2
    else:
        for i in str2:
            if i == exp:
                # print(i)
                print("string:" + exp + " match {}".format(i))
                return i
                break
            else:
                continue



print(solution('GGHDFS','T'))

# list_str=['s','w','g','h']
# for i in list_str:
#     if i == 'g':
#        print(i)
#     else:
#         print("123")
