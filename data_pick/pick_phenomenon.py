import xlwt

import util.util as util
def get_phenomenon():
    phenomenon_src = []
    phenomenon_out = []
    type_dict = []
    type_out = []
    temp_list = []
    type_dict = util.get_type_list()

    table = util.get_modified_data()
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            phenomenon_src.append(table.row_values(i)[4])

    for p in phenomenon_src:
        list = util.get_list_by_enter(p)
        for l in list:
            if l == ";snomedct:;;;;" or l == "":
                continue
            first_colon = l.index(':')
            first_semicolon = l.index(';')
            type = l[0:first_colon]
            phenomenon = l[first_colon + 1:first_semicolon]
            temp = type + ":" + phenomenon
            try:
                temp_list.index(temp)
            except:
                temp_list.append(temp)
                type_out.append(type)
                phenomenon_out.append(phenomenon)
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet1.write(0, 0, 'pid')
    sheet1.write(0, 1, 'phenomenon')
    sheet1.write(0, 2, 'type')
    sheet1.write(0, 3, 'tid')
    for i in range(len(phenomenon_out)):
        # print(result[i][j])
        try:
            sheet1.write(i + 1, 0, i + 1)
            sheet1.write(i + 1, 1, phenomenon_out[i])
            sheet1.write(i + 1, 2, type_out[i])
            sheet1.write(i + 1, 3, type_dict.index(type_out[i])+1)
        except:
            print(i, phenomenon_out[i], ":", type_out[i])
    wb.save("../final_data/phenomenon.xls")

    print("end")
