#!/usr/bin/env python3
#-*- encoding=utf-8 -*-
import sys
from collections import namedtuple
# 税率表条目类，该类由namedtuple动态创建，代表一个命名元组
IncomeTaxQuickLookupItem = namedtuple(
        'IncomeTaxQuickLookupItem',
        ['start_point','tax_rate','quick_subtractor']
        )

# 起征点常量
INCOME_TAX_START_POINT = 5000

# 税率表，里面的元素类型为前面创建的IncomeTaxQuickLookupItem
INCOME_TAX_QUICK_LOOKUP_TABLE = [
        IncomeTaxQuickLookupItem(80000,0.45,15160),
        IncomeTaxQuickLookupItem(55000,0.35,7160),
        IncomeTaxQuickLookupItem(35000,0.30,4410),
        IncomeTaxQuickLookupItem(25000,0.25,2660),
        IncomeTaxQuickLookupItem(12000,0.2,1410),
        IncomeTaxQuickLookupItem(3000,0.1,210),
        IncomeTaxQuickLookupItem(0,0.03,0),
        ]

# 各种社保缴费比例常量
SOCIAL_INSURANCE_MONEY_RATE = {
        'endowment_insurance': 0.08,
        'medical_insurance': 0.02,
        'unemployment_insurance': 0.005,
        'employment_injury_insurance': 0,
        'maternity_insurance': 0,
        'public_accumulation_funds': 0.06
        }

def calc_income_tax_and_remain(income):
# 计算扣除社保缴费和起征点之后的应纳税额
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT


    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax),'{:.2f}'.format(real_income - tax)
    return '0.00','{:.2f}'.format(real_income)
def main():


    for  item in sys.argv[1:]:
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print("Parameter Error")
            continue

        _, remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id, remain))

if __name__ == '__main__':
    main()
