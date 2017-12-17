__author__ = 'hill'

import tushare as ts

def get_datas_single(indexName):
    '''
    get tushare info
    :param indexName:
    :return:
    '''
    indexK = ts.get_k_data(indexName, index=True)
    return indexK




