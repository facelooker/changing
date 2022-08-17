import xlrd
import xlwt
"""
获取文件对象
"""
data = xlrd.open_workbook('pyt.xls')
#通过index获取第一个sheet
"""
读文件，获取sheet对象
"""
table = data.sheets()[0]
#获取所有sheet
table_name = data.sheet_names()
#通过sheetname获取sheets
table_name_by_name = data.sheet_by_name("Sheet1")


#获取行数据
n_rows = table.nrows
#获取行数据
n_cols = table.ncols
#获取所有行数据
for i in range(n_rows):
    if i == 0: #剔除第一行
        continue
    # print(table.row_values(i))
    # print(table.row_values(i)[0:2])#截取前两列
#获取所有列数据
for i in range(n_cols):
    # print(table.col_values(i))
    pass

#遍历单元格cell
for i in range(n_rows):
    if i ==0:
        continue
    for y in range(n_cols):
        # print(table.cell_value(i,y))
        pass

"""
写文件，获取对象
"""

wbt = xlwt.Workbook()
#创建sheet页
sheet = wbt.add_sheet("wbt_sheet1")
sheet.write(0,0,'wbt_sheet1')#第0行，第0列，value=wbt_sheet1
wbt.save("wbt_sheet1.xls")#保存文件

