# 提取遗传方式
import xlwt
import xlrd
import re
import util.util as util
def get_inheritance():
    table = util.get_modified_data()
    minnumber = []
    inheritance = []
    inheritance_result=[]
    for i in range(table.nrows):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        else:
            inheritance.append(table.row_values(i)[2])
    new_inheritance = []
    for t in inheritance:
        index = 0
        try:
            index = t.index(';')
        except:
            index = len(t)
        if index < len(t):
            new_inheritance.append(t[:index])
        else:
            new_inheritance.append(t)
    for i in new_inheritance:  # 循环逐行打印
        tmp = i
        if tmp =='':
            continue
        if tmp not in inheritance_result:
            inheritance_result.append(tmp)
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('inheritance')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'name')
    for i in range(len(inheritance_result)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, inheritance_result[i])
    wb.save("../final_data/inheritance.xls")
