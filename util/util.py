# 黄伟 2018-331
import time
import xlrd

RAW_DATA_FILE = "../raw_data/omim_phenotype_20180331_hw.xls"
MODIFIED_DATA_FILE = "../final_data/omim_phenotype_modified.xls"
TYPE_DATA_FILE = "../raw_data/type.xls"


# 获取当前日期，用于写入文件名称
def get_current_date():
    current_date = time.strftime("%Y%m%d")
    return current_date


# 获取原始数据，即文件中的第一张表
def get_raw_data():
    file = xlrd.open_workbook(RAW_DATA_FILE)
    table = file.sheets()[0]  # 打开第一张表
    return table


# 获取excel数据
def get_file_data(filename):
    file = xlrd.open_workbook(filename)
    table = file.sheets()[0]  # 打开第一张表
    return table


# 按行获取数据，返回list
def get_list_by_enter(str):
    list = str.split('\n')
    return list


# 按分号分隔，返回list
def get_list_by_semicolon(str):
    list = str.split(';')
    return list
# 按分号分隔，返回list
def get_list_by_colon(str):
    list = str.split(',')
    return list



# 获取部位列表
def get_type_list():
    type_list = []
    data = xlrd.open_workbook(TYPE_DATA_FILE)  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):
        type_list.append(table.row_values(i)[0])
    return type_list


# 获取预处理之后的数据
def get_modified_data():
    file = xlrd.open_workbook(MODIFIED_DATA_FILE)
    table = file.sheets()[0]  # 打开第一张表
    return table
