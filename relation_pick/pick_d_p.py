import xlrd
import xlwt
import time
import util.util as util
def get_d_p():
    phenomenon_in = []
    mimnumber_in = []
    mimnumber_out = []
    phenomenon_out = []
    phenomenon_dict = []
    data = xlrd.open_workbook('../final_data/phenomenon.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数

    for i in range(nrows):
        if i == 0:
            continue
        else:
            phenomenon_dict.append(table.row_values(i)[2] + ":" + table.row_values(i)[1])
    table1 = util.get_modified_data()
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            phenomenon_in.append(table1.row_values(i)[4])
            mimnumber_in.append(table1.row_values(i)[0])
    count = 0
    for p in phenomenon_in:
        mimnumber = mimnumber_in[count]
        list = util.get_list_by_enter(p)

        for l in list:
            if l == ";snomedct:;;;;" or l == "":
                list.remove(l)

        if len(list) == 0:
            phenomenon_out.append(p)
            mimnumber_out.append(mimnumber)
            count = count + 1
            continue
        for l in list:
            phenomenon_out.append(l)
            mimnumber_out.append(mimnumber)
        count = count + 1
    wb = xlwt.Workbook()
    for j in range(3):
        sheet_name = 'sheet' + str(j + 1)
        sheet1 = wb.add_sheet(sheet_name)
        sheet1.write(0, 0, 'mimnumber')
        sheet1.write(0, 1, 'pid')
        for i in range(30000):
            if j * 30000 + i < len(mimnumber_out):
                sheet1.write(i + 1, 0, mimnumber_out[j * 30000 + i])
                try:
                    sheet1.write(i + 1, 1, phenomenon_dict.index(
                        phenomenon_out[j * 30000 + i][:phenomenon_out[j * 30000 + i].index(';')]) + 1)
                except:
                    sheet1.write(i + 1, 1, ":")
            else:
                break

        # sheet1.write(i + 1, 2, dict.index(type_out[i])+1)
    wb.save("../final_data/d_p_relationship.xls")

    print("end")
