import xlrd
import xlwt
import time
import util.util as util


def get_all():
    # 获取需要的数据
    type_dict = util.get_type_list()
    raw_data = util.get_modified_data()
    current_date = util.get_current_date()

    phenomenon_src = []
    phenomenon_dst = []
    type_dst = []
    system_dst = []

    for i in range(raw_data.nrows):
        if i == 0:
            continue
        else:
            phenomenon_src.append(raw_data.row_values(i)[4])

    for p in phenomenon_src:
        list = util.get_list_by_enter(p)
        for l in list:
            if l == ";snomedct:;;;;" or l == "":
                continue
            first_colon = l.index(':')
            first_semicolon = l.index(';')
            type = l[0:first_colon]  # 获取疾病部位
            phenomenon = l[0:first_semicolon]  # 获取疾病描述
            system = l[first_semicolon + 1:]  # 获取各个系统的所有信息
            # 此处假设对相同部位相同表型，只有一种描述
            try:
                phenomenon_dst.index(phenomenon)
            except:
                type_dst.append(type)
                phenomenon_dst.append(phenomenon)
                system_dst.append(system)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'pid')
    sheet1.write(0, 1, 'phenomenon')
    sheet1.write(0, 2, 'type')
    sheet1.write(0, 3, 'system')
    sheet1.write(0, 4, 'snomedct')
    sheet1.write(0, 5, 'UMLS')
    sheet1.write(0, 6, 'ICD10CM')
    sheet1.write(0, 7, 'ICD9Cm')
    sheet1.write(0, 8, 'HPO')
    for i in range(len(phenomenon_dst)):
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, phenomenon_dst[i])
            sheet1.write(i + 1, 2, type_dict.index(type_dst[i]) + 1)
            sheet1.write(i + 1, 3, system_dst[i])
            list = util.get_list_by_semicolon(system_dst[i])
            sheet1.write(i + 1, 4, list[0])
            sheet1.write(i + 1, 5, list[1])
            sheet1.write(i + 1, 6, list[2])
            sheet1.write(i + 1, 7, list[3])
            sheet1.write(i + 1, 8, list[4])
        except:
            print(i, phenomenon_dst[i], ":", type_dst[i])
    wb.save("../final_data/system.xls")
    print("end")


def get_snomedct():
    current_date = util.get_current_date()
    table = util.get_file_data('../final_data/system.xls')
    src = []
    dst = []
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            src.append(table.row_values(i)[4])

    for item in src:
        item = item[item.index(":") + 1:]
        list = util.get_list_by_colon(item)
        for l in list:
            if l == "":
                continue
            else:
                try:
                    dst.index(l)
                except:
                    dst.append(l)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'sid')
    sheet1.write(0, 1, 'snomedct')

    for i in range(len(dst)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, dst[i])
        except:
            print(i, dst[i])
    wb.save("../final_data/snomect.xls")
    print("end")


def get_umls():
    current_date = util.get_current_date()
    table = util.get_file_data('../final_data/system.xls')
    src = []
    dst = []
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            src.append(table.row_values(i)[5])

    for item in src:
        if item=="":
            continue
        list = util.get_list_by_colon(item)
        for l in list:
            if l == "":
                continue
            else:
                try:
                    dst.index(l)
                except:
                    dst.append(l)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'uid')
    sheet1.write(0, 1, 'umls')

    for i in range(len(dst)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, dst[i])
        except:
            print(i, dst[i])
    wb.save("../final_data/umls.xls")
    print("end")


def get_ICD9():
    current_date = util.get_current_date()
    table = util.get_file_data('../final_data/system.xls')
    src = []
    dst = []
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            src.append(table.row_values(i)[7])

    for item in src:
        if item=="":
            continue
        item = item[item.index(":") + 1:]
        list = util.get_list_by_colon(item)
        for l in list:
            if l == "":
                continue
            else:
                try:
                    dst.index(l)
                except:
                    dst.append(l)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'i9id')
    sheet1.write(0, 1, 'icd9cm')

    for i in range(len(dst)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, dst[i])
        except:
            print(i, dst[i])
    wb.save("../final_data/ICD9CM.xls")
    print("end")


def get_ICD10():
    current_date = util.get_current_date()
    table = util.get_file_data('../final_data/system.xls')
    src = []
    dst = []
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            src.append(table.row_values(i)[6])

    for item in src:
        if item=="":
            continue
        item = item[item.index(":") + 1:]
        list = util.get_list_by_colon(item)
        for l in list:
            if l == "":
                continue
            else:
                try:
                    dst.index(l)
                except:
                    dst.append(l)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'i10id')
    sheet1.write(0, 1, 'icd10cm')

    for i in range(len(dst)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, dst[i])
        except:
            print(i, dst[i])
    wb.save("../final_data/ICD10CM.xls")
    print("end")


def get_hpo():
    current_date = util.get_current_date()
    table = util.get_file_data('../final_data/system.xls')
    src = []
    dst = []
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            src.append(table.row_values(i)[8])

    for item in src:
        if item=="":
            continue
        item = item[item.index(":") + 1:]
        list = util.get_list_by_colon(item)
        for l in list:
            if l == "":
                continue
            else:
                try:
                    dst.index(l)
                except:
                    dst.append(l)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'hid')
    sheet1.write(0, 1, 'hpo')

    for i in range(len(dst)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, dst[i])
        except:
            print(i, dst[i])
    wb.save("../final_data/HPO.xls")
    print("end")
