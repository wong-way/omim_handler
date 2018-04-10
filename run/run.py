from data_prehandle.prehandler import *
from data_pick.pick_inheritance import *
from data_pick.pick_phenomenon import *
from data_pick.pick_system_dict import *
from data_pick.pick_gene import *
from data_pick.pick_disease import *
from relation_pick.pick_system import *
from relation_pick.pick_d_p import *
from relation_pick.pick_g_d import *

# 数据预处理
prehandler()
# 选出基因
get_gene()
# 选出遗传方式
get_inheritance()
# 获取系统信息
get_all()
get_hpo()
get_ICD10()
get_ICD9()
get_snomedct()
get_umls()
# 选出疾病信息
get_disease()
# 选出表型
get_phenomenon()

# 选出疾病表型联系集
get_d_p()
# 选出疾病基因联系集
get_g_d()
# 选出各个系统的联系集
get_r_hpo()
get_r_icd9()
get_r_icd10()
get_r_snomect()
get_r_umls()
print("处理完毕")