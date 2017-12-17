__author__ = 'hill'

from zhishu.commons import constant_indexs
from zhishu.get_datas import get_datas_single
from zhishu.analysis_datas import analysis_single

def process():
    for index_code,index_value in constant_indexs.focus_indexs.items():
        index_DF = get_datas_single.get_datas_single(index_code)
        std_z = analysis_single.analysis_single(index_DF)
        print(type(std_z))
        print("%s-index:%s ----- zscore:%s"%(index_value,index_code, std_z))


if __name__ == '__main__':
    process()