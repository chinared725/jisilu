import csv
import pandas as pd
import numpy as np
from open_url_get_data import *
from utils import *

class CbEb:

    def __init__(self):
        self.url = "https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1584777951900"
        self.data = get_data(self.url)

    def get_cb_data(self):

        data = data_remove_percent(self.data, ['convert_amt_ratio', 'premium_rt', 'sincrease_rt', 'ytm_rt', 'ytm_rt_tax', 'increase_rt'])
        data['turnover_rate'] = data['turnover_rt'] * 0.01
        data['报价时间'] = data['price_tips'].apply(get_bond_time)

        data.drop(['adjust_tip',
                   'adjusted',
                   'apply_cd',
                   'fund_rt',
                   'last_time',
                   'left_put_year',
                   'margin_flg',
                   'noted',
                   'online_offline_ratio',
                   'option_tip',
                   'owned',
                   'pre_bond_id',
                   'put_notes',
                   'qflag',
                   'qflag2',
                   'qstatus',
                   'real_force_redeem_price',
                   'ref_yield_info',
                   'repo_cd',
                   'sqflg',
                   'stock_cd',
                   'stock_net_value',
                   'price',
                   'put_dt',
                   'put_inc_cpn_fl',
                   'put_total_days',
                   'rating_cd',
                   'ration',
                   'redeem_dt',
                   'redeem_inc_cpn_fl',
                   'repo_valid',
                   'repo_valid_from',
                   'repo_valid_to',
                   'ration_cd',
                   'turnover_rt'], axis=1, inplace=True)

        cols = {'adj_cnt':'下调次数',
                'adj_scnt':'下调成功次数',
                'convert_cd':'转债占比',
                'convert_cd_tip':'转股提示',
                'convert_dt':'转股期开始',
                'convert_price':'转股价',
                'convert_price_valid':'转股价有效性',
                'convert_price_valid_from':'转债价格生效日',
                'convert_value':'转股价值',
                'curr_iss_amt':'当前规模_亿',
                'dblow':'双低',
                'force_redeem':'最后交易日',
                'force_redeem_price':'强赎股价',
                'full_price':'转债价格',
                'guarantor':'担保',
                'issuer_rating_cd':'评级',
                'maturity_dt':'到期日',
                'next_put_dt':'回售日',
                'orig_iss_amt':'原始规模_亿',
                'put_convert_price':'回售股价',
                'put_convert_price_ratio':'回售价与股价比',
                'put_count_days':'回售天', 'put_price':'回售价',
                'put_real_days':'回售剩余天数',
                'ration_rt':'股东配售率',
                'redeem_count_days':'强赎连续日',
                'redeem_flag':'是否行使强赎',
                'redeem_icon':'是否达到强赎标准',
                'redeem_price':'强赎价',
                'redeem_price_ratio':'强赎转股价值',
                'redeem_real_days':'满足强赎日',
                'redeem_style':'满足后是否强赎',
                'redeem_total_days':'强赎总日数',
                'repo_discount_rt':'折算率',
                'short_maturity_dt':'到期日',
                'sprice':'正股现价',
                'stock_id':'正股代码',
                'stock_nm':'正股名字',
                'svolume':'正股成交额_万',
                'total_shares':'总股本',
                'turnover_rate':'换手率',
                'volume':'可转债成交_万',
                'year_left':'剩余年限',
                'convert_amt_ratio':'可转债_股票市值比',
                'premium_rt':'溢价率',
                'sincrease_rt':'正股涨幅',
                'ytm_rt':'年化税前收益率',
                'ytm_rt_tax':'年化税后收益率',
                'bond_id':'转债代码',
                'bond_nm':'转债名称',
                'increase_rt':'转债涨幅',
                'price_tips':'上市状态'}

        data.rename(columns=cols, inplace=True)

        cb = data[data['转债名称'].apply(lambda x : 'EB' not in x)]



        cb = cb[['转债代码',
                 '转债名称',
                 '转债价格',
                 '正股名字',
                 '正股现价',
                 '转股价',
                 '转股价值',
                 '溢价率',
                 '转债涨幅',
                 '正股涨幅',
                 '评级',
                 '剩余年限',
                 '当前规模_亿',
                 '原始规模_亿',
                 '双低',
                 'pb',
                 '换手率',
                 '上市状态',
                 '下调次数',
                 '下调成功次数']].sort_values(by=['转债价格', '溢价率'])   #sort the dataframe by price and premium rate

        return cb

    def get_eb_data(self):
        data = data_remove_percent(self.data, ['convert_amt_ratio', 'premium_rt', 'sincrease_rt', 'ytm_rt', 'ytm_rt_tax', 'increase_rt'])
        data['turnover_rate'] = data['turnover_rt'] * 0.01
        data['报价时间'] = data['price_tips'].apply(get_bond_time)

        data.drop(['adjust_tip',
                   'adjusted',
                   'apply_cd',
                   'fund_rt',
                   'last_time',
                   'left_put_year',
                   'margin_flg',
                   'noted',
                   'online_offline_ratio',
                   'option_tip',
                   'owned',
                   'pre_bond_id',
                   'put_notes',
                   'qflag',
                   'qflag2',
                   'qstatus',
                   'real_force_redeem_price',
                   'ref_yield_info',
                   'repo_cd',
                   'sqflg',
                   'stock_cd',
                   'stock_net_value',
                   'price',
                   'put_dt',
                   'put_inc_cpn_fl',
                   'put_total_days',
                   'rating_cd',
                   'ration',
                   'redeem_dt',
                   'redeem_inc_cpn_fl',
                   'repo_valid',
                   'repo_valid_from',
                   'repo_valid_to',
                   'ration_cd',
                   'turnover_rt'], axis=1, inplace=True)

        cols = {'adj_cnt':'下调次数',
                'adj_scnt':'下调成功次数',
                'convert_cd':'转债占比',
                'convert_cd_tip':'转股提示',
                'convert_dt':'转股期开始',
                'convert_price':'转股价',
                'convert_price_valid':'转股价有效性',
                'convert_price_valid_from':'转债价格生效日',
                'convert_value':'转股价值',
                'curr_iss_amt':'当前规模_亿',
                'dblow':'双低',
                'force_redeem':'最后交易日',
                'force_redeem_price':'强赎股价',
                'full_price':'转债价格',
                'guarantor':'担保',
                'issuer_rating_cd':'评级',
                'maturity_dt':'到期日',
                'next_put_dt':'回售日',
                'orig_iss_amt':'原始规模_亿',
                'put_convert_price':'回售股价',
                'put_convert_price_ratio':'回售价与股价比',
                'put_count_days':'回售天', 'put_price':'回售价',
                'put_real_days':'回售剩余天数',
                'ration_rt':'股东配售率',
                'redeem_count_days':'强赎连续日',
                'redeem_flag':'是否行使强赎',
                'redeem_icon':'是否达到强赎标准',
                'redeem_price':'强赎价',
                'redeem_price_ratio':'强赎转股价值',
                'redeem_real_days':'满足强赎日',
                'redeem_style':'满足后是否强赎',
                'redeem_total_days':'强赎总日数',
                'repo_discount_rt':'折算率',
                'short_maturity_dt':'到期日',
                'sprice':'正股现价',
                'stock_id':'正股代码',
                'stock_nm':'正股名字',
                'svolume':'正股成交额_万',
                'total_shares':'总股本',
                'turnover_rate':'换手率',
                'volume':'可转债成交_万',
                'year_left':'剩余年限',
                'convert_amt_ratio':'可转债_股票市值比',
                'premium_rt':'溢价率',
                'sincrease_rt':'正股涨幅',
                'ytm_rt':'年化税前收益率',
                'ytm_rt_tax':'年化税后收益率',
                'bond_id':'转债代码',
                'bond_nm':'转债名称',
                'increase_rt':'转债涨幅',
                'price_tips':'上市状态'}

        data.rename(columns=cols, inplace=True)

        eb =  data[data['转债名称'].apply(lambda x : 'EB' in x)]

        eb = eb[['转债代码',
                 '转债名称',
                 '转债价格',
                 '正股现价',
                 '转股价',
                 '转股价值',
                 '溢价率',
                 '转债涨幅',
                 '正股涨幅',
                 '评级',
                 '剩余年限',
                 '当前规模_亿',
                 '原始规模_亿',
                 '双低',
                 '正股名字',
                 '正股现价',
                 'pb',
                 '换手率',
                 '上市状态',
                 '下调次数',
                 '下调成功次数']].sort_values(by=['转债价格', '溢价率'])   #sort the dataframe by price and premium rate
        return eb

    def get_double_low_bond(self, bond_type='cb', bond_price=105, premium_rate=0.3,pb=0, adjusted = False):
        if bond_type.lower() == 'cb':
            data = self.get_cb_data()
        elif bond_type.lower() == 'eb':
            data = self.get_eb_data()
        else:
            raise ValueError('错误的债券类型')

        double_low = data[(data['转债价格'] < bond_price)  & (data['溢价率'] < premium_rate) \
         & (data['上市状态']!='待上市') & (data['pb'] > pb)]    # find cb with price lower than 105, premium rate <0.3 and pb>1

        if adjusted:
            double_low = data[(data['下调次数']>=1) & (data['转债价格'] < bond_price) \
             & (data['溢价率']<premium_rate)  & (data['pb'] > pb)].sort_values(by=['转债价格', '溢价率'])  # find cb with price lower than 105, premium rate <0.3 and pb>1 and ajust for at lease one time
        return double_low

    def get_bond_not_list(self, bond_type='cb'):
        if bond_type.lower() == 'cb':
            data = self.get_cb_data()
        elif bond_type.lower() == 'eb':
            data = self.get_eb_data()
        else:
            raise ValueError('错误的债券类型')
        bond_not_list = data[data['上市状态']=='待上市'].sort_values(by=['转股价值'])
        return bond_not_list