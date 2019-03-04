#!/usr/bin/env python3
import sys
import csv
from collections import namedtuple
IncomeTaxQuickLookup = namedtuple('IncomeTaxQuickLookup',
        ['start_point','tax_rate','quick_num']
        )
IncomeTaxQuickLookupTable = [
        IncomeTaxQuickLookup(80000,0.45,15160),
        IncomeTaxQuickLookup(55000,0.35,7160),
        IncomeTaxQuickLookup(35000,0.3,4410),
        IncomeTaxQuickLookup(25000,0.25,2660),
        IncomeTaxQuickLookup(12000,0.2,1410),
        IncomeTaxQuickLookup(3000,0.1,210),
        IncomeTaxQuickLookup(0,0.03,0)
        ]
INCOME_TAX_START_POINT = 5000
#处理命令行参数
class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def _get_path(self,option):
        index = self.args.index(option)
        return self.args[index+1]
    @property
    def config_path(self):
        return self._get_path('-c')
    @property
    def userdata_path(self):
        return self._get_path('-d')
    @property
    def out_path(self):
        return self._get_path('-o')

args = Args()

class Config(object):
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}

        with open(args.config_path) as f:
            for line in f.readline():
                key, value = line.strip().split('=')
                config[key.strip()] = float(value.strip())
        return config
    def _get_config(self,key):
        return self.config[key]
    @property
    def insurance_basic_low(self):
        return self._get_config('JiShuL')
    @property
    def insurance_basic_high(self):
        return self._get_config('JiShuH')
    @property
    def social_insurance_rate(self):
        return sum([self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')
            ])
config = Config()
class UserData(object):

    def __init__(self):
        self.userdata = self._read_user_data()

    def _read_users_data(self):
        userdata = []
        with open(args.userdata_path) as f:
            for line in f.readline():
                employee_id, income = line.strip().split(':')
                userdata.append((employee_id,income))
        return userdata
    def get_userdata(self):
        return self.userdata
class IncomeTaxCalculator(object):
    def __init__(self,userdata):
        self.userdata = userdata

    @classmethed
    def calc_social_insurance_money(cls,income):
        if income < config.insurance_basic_low:
            return config.insurance_basic_low * social_insurance_rate
        elif income > config.insurance_basic_high:
            return  config.insurance_basic_high * social_insurance_rate
        else:
            return income * social_insurance_rate
    @classmethed
    def calc_income_tax_and_remain(cls,income):
        social_insurance_money = cls.calc_social_insurance_money(income)
        real_income = income - social_insurance_money
        tax_part = real_income - INCOME_TAX_START_POINT
        for item in IncomeTaxQuickLookupTable:
            if tax_part > item.start_point:
                tax = tax_part * item.tax_rate - item.quick_num
                return '{:.2f}'.format(tax),'{:.2f}'.format(real_income-tax)
        return '0.00','{:.2f}'.formant(real_income)

        
    def calc_for_all_userdata(self):
        result = []
        for employee_id,income in self.userdata.get_userdata():
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income))
            tax,remain = self.calc_income_tax_and_ramain(income)
            result.append([employee_id,income,social_insurance_money,tax,remain])
        return result
    def export(self,default='csv'):
        result = self.calc_for_all_userdata()
        with open(args.out_path,'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    calcutor = IncomeTaxCalculator(Userdata())
    calcutor.export()
            




