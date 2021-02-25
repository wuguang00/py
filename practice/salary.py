#!/usr/bin/python3

# input format: ./salary.py 0 or ./salary.py 1
# 2021, Shanghai, Shebao and Gongjj

import sys
num  = []
sval = []

#填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
def tax(salary_pre, pension_insurance, medical_insurance, unemployment_insurance, housing_fund, deduction):
    """根据税前月薪, 社保, 医疗保险, 失业保险, 公积金, 专项扣除
    算出2020每月应交税额"""

    sval=salary_pre
    salmax = 28017
    shebao = 0
    yiliao = 0
    shiye = 0
    gongjj = 0
    bcgjj = 0

    if (sval*0.08 > salmax * 0.08):
        shebao = salmax * 0.08
    else:
        shebao=sval*0.08

    if (sval*0.02 > salmax * 0.02):
        yiliao = salmax * 0.02
    else:
        yiliao=sval*0.02
    if (sval*0.005 > salmax * 0.005):
        shiye = salmax * 0.005
    else:
        shiye=sval*0.005
    if (sval*0.07 > salmax * 0.07):
        gongjj = salmax * 0.07
    else:
        gongjj = sval*0.07
    if (sval * 0.05 > salmax * 0.05):
        bcgjj = salmax * 0.05
    else:
        bcgjj= sval * 0.05

    if sys.argv[1] == "1":
        temp = salary_pre - shebao - yiliao - shiye - gongjj - bcgjj - 5000 - deduction
    else:
        temp = salary_pre - shebao - yiliao - shiye - gongjj - 5000 - deduction
        bcgjj = 0

    month1 = []
    count = 0
    # 计算新税
    for i in range(1, 13):
        k = int(temp * i)
        if k <= 0:
            rate_tax = 0
            part_tax = 0
        elif 0 < k <= 36000:
            rate_tax = 0.03
            part_tax = 0
        elif 36000 < k <= 144000:
            rate_tax = 0.1
            part_tax = 2520
        elif 144000 < k <= 300000:
            rate_tax = 0.2
            part_tax = 16920
        elif 300000 < k <= 420000:
            rate_tax = 0.25
            part_tax = 31920
        elif 420000 < k <= 660000:
            rate_tax = 0.3
            part_tax = 52920
        elif 660000 < k <= 960000:
            rate_tax = 0.35
            part_tax = 85920
        elif k > 960000:
            rate_tax = 0.45
            part_tax = 181920

        month1.append(temp * i * rate_tax - part_tax - count)
        count += month1[i-1]
        print("tax: {:.2f}".format(count))

        # print("{}:pension_insurance:       {}".format(i, shebao))
        # print("{}:medical_insurance:       {}".format(i, yiliao))
        # print("{}:unemployment_insurance:  {}".format(i, shiye))
        # print("{}:housing_fund:            {}".format(i, gongjj))
        # print("The {}, you get the salary: {:.2f}".format(i, salary_pre - shebao - yiliao - shiye - gongjj - month1[i-1]))

    print("     社保    医疗保险 失业保险  公积金  补充公积金    税后     缴税")
    for i in range(1, 13):
        print("{:2} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:12.2f} {:8.2f}".format(i, shebao, yiliao, shiye, gongjj, bcgjj, salary_pre-shebao-yiliao-shiye-gongjj-bcgjj-month1[i-1], month1[i-1]))
    year = round(sum(month1), 2)
    print(year)
    month = [round(i, 2) for i in month1]
    print(month)

#填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
tax(28800, 0.08, 0.02, 0.005, 0.12, 1000)





