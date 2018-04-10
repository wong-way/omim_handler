import xlrd
import xlwt
import time
import util.util as util
def get_r_hpo():
    # 存hpo字典
    hpo_dict = []

    data = xlrd.open_workbook('../final_data/HPO.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        if i == 0:
            continue
        else:
            hpo_dict.append(table.row_values(i)[1])

    hpo_in = []
    pid_in = []
    pid_out = []
    hid_out = []
    data1 = xlrd.open_workbook('../final_data/system.xls')  # 打开xls文件
    table1 = data1.sheets()[0]  # 打开第一张表
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            hpo_in.append(table1.row_values(i)[8])
            pid_in.append(table1.row_values(i)[0])
    index = 0
    for d in hpo_in:
        try:
            d = d[d.index(":") + 1:]
        except:
            pid_out.append(pid_in[index])
            hid_out.append(-1)
        else:
            list = util.get_list_by_colon(d)
            for l in list:
                if l == "":
                    continue
                pid_out.append(pid_in[index])
                hid_out.append(hpo_dict.index(l) + 1)
        index = index + 1

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'pid')
    sheet1.write(0, 2, 'hid')

    for i in range(len(pid_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, pid_out[i])
            sheet1.write(i + 1, 2, hid_out[i])
        except:
            print(i, pid_out[i])
    wb.save("../final_data/hpo_relationship.xls")

    print("end")
def get_r_icd9():

    # 存icd9字典
    icd9_dict = []
    data = xlrd.open_workbook('../final_data/ICD9CM.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        if i == 0:
            continue
        else:
            icd9_dict.append(table.row_values(i)[1])

    hpo_in = []
    pid_in = []
    pid_out = []
    hid_out = []
    data1 = xlrd.open_workbook('../final_data/system.xls')  # 打开xls文件
    table1 = data1.sheets()[0]  # 打开第一张表
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            hpo_in.append(table1.row_values(i)[7])
            pid_in.append(table1.row_values(i)[0])
    index = 0
    for d in hpo_in:
        try:
            d = d[d.index(":") + 1:]
        except:
            pid_out.append(pid_in[index])
            hid_out.append(-1)
        else:
            list = util.get_list_by_colon(d)
            for l in list:
                if l == "":
                    continue
                pid_out.append(pid_in[index])
                hid_out.append(icd9_dict.index(l) + 1)
        index = index + 1

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'pid')
    sheet1.write(0, 2, 'i9id')

    for i in range(len(pid_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, pid_out[i])
            sheet1.write(i + 1, 2, hid_out[i])
        except:
            print(i, pid_out[i])
    wb.save("../final_data/ICD9CM_relationship.xls")

    print("end")
def get_r_icd10():
    icd10_dict = []
    data = xlrd.open_workbook('../final_data/ICD10CM.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        if i == 0:
            continue
        else:
            icd10_dict.append(table.row_values(i)[1])
    icd10_in = []
    pid_in = []
    pid_out = []
    icd10_out = []
    data1 = xlrd.open_workbook('../final_data/system.xls')  # 打开xls文件
    table1 = data1.sheets()[0]  # 打开第一张表
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            icd10_in.append(table1.row_values(i)[6])
            pid_in.append(table1.row_values(i)[0])
    index = 0
    for d in icd10_in:
        try:
            d = d[d.index(":") + 1:]
        except:
            pid_out.append(pid_in[index])
            icd10_out.append(-1)
        else:
            list = util.get_list_by_colon(d)
            for l in list:
                if l == "":
                    continue
                pid_out.append(pid_in[index])
                icd10_out.append(icd10_dict.index(l) + 1)
        index = index + 1

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'pid')
    sheet1.write(0, 2, 'i10id')

    for i in range(len(pid_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, pid_out[i])
            sheet1.write(i + 1, 2, icd10_out[i])
        except:
            print(i, pid_out[i])
    wb.save("../final_data/ICD10CM_relationship.xls")

    print("end")
def get_r_umls():

    # 存hpo字典
    hpo_dict = []
    data = xlrd.open_workbook('../final_data/umls.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        if i == 0:
            continue
        else:
            hpo_dict.append(table.row_values(i)[1])

    hpo_in = []
    pid_in = []
    pid_out = []
    hid_out = []
    data1 = xlrd.open_workbook('../final_data/system.xls')  # 打开xls文件
    table1 = data1.sheets()[0]  # 打开第一张表
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            hpo_in.append(table1.row_values(i)[5])
            pid_in.append(table1.row_values(i)[0])
    index = 0
    for d in hpo_in:
        list = util.get_list_by_colon(d)
        if list[0] == "":
            pid_out.append(pid_in[index])
            hid_out.append(-1)
        for l in list:
            if l == "":
                continue
            pid_out.append(pid_in[index])
            hid_out.append(hpo_dict.index(l) + 1)
        index = index + 1

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'pid')
    sheet1.write(0, 2, 'sid')

    for i in range(len(pid_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, pid_out[i])
            sheet1.write(i + 1, 2, hid_out[i])
        except:
            print(i, pid_out[i])
    wb.save("../final_data/UMLS_relationship.xls")

    print("end")
def get_r_snomect():

    snomect_dict = []
    data = xlrd.open_workbook('../final_data/snomect.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        if i == 0:
            continue
        else:
            snomect_dict.append(table.row_values(i)[1])

    snomect_in = []
    pid_in = []
    pid_out = []
    snomect_out = []
    data1 = xlrd.open_workbook('../final_data/system.xls')  # 打开xls文件
    table1 = data1.sheets()[0]  # 打开第一张表
    nrows1 = table1.nrows  # 获取表的行数
    for i in range(nrows1):
        if i == 0:
            continue
        else:
            snomect_in.append(table1.row_values(i)[4])
            pid_in.append(table1.row_values(i)[0])
    index = 0
    for d in snomect_in:

        d = d[d.index(":") + 1:]

        list = util.get_list_by_colon(d)
        if list[0] == "":
            pid_out.append(pid_in[index])
            snomect_out.append(-1)
        for l in list:
            if l == "":
                continue
            pid_out.append(pid_in[index])
            snomect_out.append(snomect_dict.index(l) + 1)
        index = index + 1

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'pid')
    sheet1.write(0, 2, 'sid')

    for i in range(len(pid_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, pid_out[i])
            sheet1.write(i + 1, 2, snomect_out[i])
        except:
            print(i, pid_out[i])
    wb.save("../final_data/SNOMECT_relaitonship.xls")
    print("end")
