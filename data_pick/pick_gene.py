# 获取基因实体信息
import xlwt
import re
import util.util as util
def get_gene():
    table = util.get_modified_data()
    gene_list = []
    id_list = []
    current_date = util.get_current_date()
    pattern = re.compile('[A-Za-z0-9]*-*[A-Za-z0-9]*,\s*\{[0-9]*\.?[0-9]*\}')
    for i in range(table.nrows):  # 循环逐行打印
        if i == 0:
            continue
        else:
            list = util.get_list_by_enter(table.row_values(i)[3])  # 获取基因数据
            for item in list:  # 对每一行数据进行处理
                if item == '\n' or item == '':
                    continue
                m = pattern.match(item)
                if m != None:
                    temp = m.group()
                    gene_list.append(temp.split(',')[0])
                    id_list.append(temp.split(',')[1][temp.split(',')[1].find('{') + 1:temp.split(',')[1].find('}')])
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('gene')
    sheet1.write(0, 0, 'id')
    sheet1.write(0, 1, 'geneName')
    sheet1.write(0, 2, 'geneNumber')
    for i in range(len(gene_list)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, gene_list[i])
        sheet1.write(i + 1, 2, id_list[i])
    wb.save("../final_data/gene.xls")
