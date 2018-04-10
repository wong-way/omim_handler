# 提取所有疾病信息


import xlrd
import xlwt
import util.util as util
def get_disease():
    table = util.get_modified_data()
    minnumber = []
    title = []
    inheritance = []
    inheritance_dict = []
    inheritance_table = util.get_file_data("../final_data/inheritance.xls")
    for i in range(inheritance_table.nrows):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        else:
            inheritance_dict.append(inheritance_table.row_values(i)[1])

    for i in range(table.nrows):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        else:
            minnumber.append(table.row_values(i)[0])
            title.append(table.row_values(i)[1])
            inheritance.append(table.row_values(i)[2])
    prefered_title = []
    shortening_title = []
    for t in title:
        index = 0
        try:
            index = t.index(';')
        except:
            index = len(t)
        if index < len(t):
            prefered_title.append(t[:index])
            shortening_title.append(t[index + 2:])
        else:
            prefered_title.append(t)
            shortening_title.append("null")
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

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('disease')
    sheet1.write(0, 0, 'mimnumber')
    sheet1.write(0, 1, 'preferredTitle')
    sheet1.write(0, 2, 'shorteningTitle')
    sheet1.write(0, 3, 'inheritance')
    sheet1.write(0, 4, 'inheritance id')
    for i in range(len(prefered_title)):
        sheet1.write(i + 1, 0, minnumber[i])
        sheet1.write(i + 1, 1, prefered_title[i])
        sheet1.write(i + 1, 2, shortening_title[i])
        sheet1.write(i + 1, 3, new_inheritance[i])
        try:
            sheet1.write(i + 1, 4, inheritance_dict.index(new_inheritance[i]) + 1)
        except:
            sheet1.write(i + 1, 4, "")

    wb.save("../final_data/disease.xls")
