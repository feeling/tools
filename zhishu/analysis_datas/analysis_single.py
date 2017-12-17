__author__ = 'hill'


def analysis_single(indexK):
    close_mean = indexK['close'].mean()
    close_std = indexK['close'].std()
    close_last = indexK.tail(1)['close'].item()
    print("close_mean:%s, close_std:%s, close_last:%s"%(close_mean, close_std, close_last))
    close_std_z = (close_last-close_mean)/close_std
    return close_std_z

