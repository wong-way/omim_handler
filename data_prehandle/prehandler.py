import xlwt
import util.util as util
def prehandler():
    current_date = util.get_current_date()

    phenomenon_src = []
    phenomenon_dst = []
    mimnumber_src = []
    preferred_title_src = []
    inheritance_src = []
    gene_src = []
    # 获取原表数据
    raw_data = util.get_raw_data()
    for i in range(raw_data.nrows):
        if i == 0:
            continue
        else:
            phenomenon_src.append(raw_data.row_values(i)[4])
            mimnumber_src.append(raw_data.row_values(i)[0])
            preferred_title_src.append(raw_data.row_values(i)[1])
            inheritance_src.append(raw_data.row_values(i)[2])
            gene_src.append(raw_data.row_values(i)[3])
    # 获取部位列表
    type_dict = util.get_type_list()

    # 处理表型，在每个表型前增加部位，并将之前多余的信息去除
    for p in phenomenon_src:
        list = util.get_list_by_enter(p)
        if list[-1] == "":
            list.pop()
        type = ''
        temp = ''
        for l in list:
            if l == ";snomedct:;;;;":
                continue
            first_colon = l.index(':')
            first_semicolon = l.index(';')
            if first_colon < first_semicolon:
                tmp = l[:first_colon]
                try:
                    type_dict.index(tmp)
                except:
                    l = type + ":" + l
                else:
                    type = tmp
            else:
                l = type + ":" + l
            temp = temp + "\n" + l;
        phenomenon_dst.append(temp)
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'mimnumber')
    sheet1.write(0, 1, 'preferredTitle')
    sheet1.write(0, 2, 'inheritance')
    sheet1.write(0, 3, 'molecularBasis')
    sheet1.write(0, 4, 'clinicalSynopsis')

    for i in range(len(phenomenon_dst)):
        sheet1.write(i + 1, 0, mimnumber_src[i])
        sheet1.write(i + 1, 1, preferred_title_src[i])
        sheet1.write(i + 1, 2, inheritance_src[i])
        sheet1.write(i + 1, 3, gene_src[i])
        sheet1.write(i + 1, 4, phenomenon_dst[i])

    wb.save("../final_data/omim_phenotype_modified.xls")

    print("modify data end")
