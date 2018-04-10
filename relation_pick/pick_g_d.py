import xlwt

import util.util as util
import re
def get_g_d():
    gene_table = util.get_file_data("../final_data/gene.xls")
    table = util.get_modified_data()
    gene_list = []
    mimnumber_result = []
    gene_result = []
    for i in range(gene_table.nrows):
        if i == 0:
            continue
        else:
            gene_list.append(gene_table.row_values(i)[1] + gene_table.row_values(i)[2])
    pattern = re.compile('[A-Za-z0-9]*-*[A-Za-z0-9]*,\s*\{[0-9]*\.?[0-9]*\}')
    for i in range(table.nrows):  # 循环逐行打印
        if i == 0:
            continue
        else:

            list = util.get_list_by_enter(table.row_values(i)[3])  # 获取基因数据
            for item in list:  # 对每一行数据进行处理
                if item == '\n' or item == '':
                    continue
                mimnumber_result.append(table.row_values(i)[0])
                m = pattern.match(item)
                if m != None:
                    temp = m.group()
                    gene = temp.split(',')[0]
                    code = temp.split(',')[1][temp.split(',')[1].find('{') + 1:temp.split(',')[1].find('}')]
                    gene_result.append(gene_list.index(gene + code) + 1)
                else:
                    gene_result.append("")
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('relationship')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'mimnumber')
    sheet1.write(0, 2, 'gid')
    for i in range(len(gene_result)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, mimnumber_result[i])
        sheet1.write(i + 1, 2, gene_result[i])
    wb.save("../final_data/g_d_relationship.xls")
