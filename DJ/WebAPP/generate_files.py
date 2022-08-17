# file_size=input("请输入想要生成文件的大小：(单位MB)")
class GenerateFile:
    def __init__(self,file_size):
        #file_size 定义文件大小
        self.file_size = str(file_size)
        self.file_path="G:\zeng\Videos\\"
        self.file_name="文件大小"+self.file_size+"MB.txt"
        #移除头尾空格，换行符
        new_file_size = self.file_size.strip()
        #字符切片，split 默认空格，换行 \n  制表 \t
        file_size_list = new_file_size.split(".")
        self.file_size_list = file_size_list

    def gennerate_file(self):
        #输入的文件大小去除首尾空格后切割，如果列表中只有一个数字说明是整数，否则就是小数
        if len(self.file_size_list) == 1:
            self.int_size_mb()
            print("文件大小{}MB,已存入地址{}".format(self.file_size,self.file_path))
        else:
            self.int_size_mb()
            self.float_size_mb()
            print("文件大小{}MB,已存入地址{}".format(self.file_size,self.file_path))
    def int_size_mb(self):
        #整数部分用写入文件w方式
        print(self.file_size_list)
        # print(int(self.file_size_list[0])
        with open(self.file_path+self.file_name,"w") as file:
            #b-kb-mb文件大小转化
            for i in range(int(self.file_size_list[0])):
                for j in range(1024):
                    file.write("01"*512)
    def float_size_mb(self):
        #小数部分用追加写入a方法
        with open(self.file_path+self.file_name,"a") as file:
            #获取小数（单位mb）
            float_size_mb=float(self.file_size)-int(self.file_size_list[0])
            for i in range(1024):
                file.write("1"*int(1024*float_size_mb))
if __name__ == '__main__':
#调用生成文件
    makedir = GenerateFile(1.6)
    makedir.gennerate_file()