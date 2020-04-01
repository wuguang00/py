#!/usr/bin/python3
# input format: ./salary.py 0 or ./salary.py 1
import sys
num = []
sval = []
i = 0

#填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
def tax(salary_pre, pension_insurance, medical_insurance, unemployment_insurance, housing_fund, deduction):
    """根据税前月薪, 社保, 医疗保险, 失业保险, 公积金, 专项扣除
    算出2019每月应交税额"""

    sval=salary_pre
    sval1 = 0
    sval2 = 0
    sval3 = 0
    sval4 = 0
    sval5 = 0
    if (sval*0.08 > 1970.7):
        sval1=1970.7
    else:
        sval1=sval*0.08
    if (sval*0.02 > 492.66):
        sval2=492.66
    else:
        sval2=sval*0.02
    if (sval*0.005 > 123.2):
        sval3=123.2
    else:
        sval3=sval*0.005
    if (sval*0.07 > 1724):
        sval4=1724
    else:
        sval4=sval*0.07
    if (sval*0.05 > 1232):
        sval5=1232
    else:
        sval5=sval*0.05

    if sys.argv[1] == "1":
        temp = salary_pre - sval1 - sval2 - sval3 - sval4 - sval5 - 5000 - deduction
    else:
        temp = salary_pre - sval1 - sval2 - sval3 - sval4 - 5000 - deduction
        sval5 = 0

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

        # print("{}:pension_insurance:       {}".format(i, sval1))
        # print("{}:medical_insurance:       {}".format(i, sval2))
        # print("{}:unemployment_insurance:  {}".format(i, sval3))
        # print("{}:housing_fund:            {}".format(i, sval4))
        # print("The {}, you get the salary: {:.2f}".format(i, salary_pre - sval1 - sval2 - sval3 - sval4 - month1[i-1]))

    print("社保 医疗保险 失业保险 公积金 补充公积金 缴税")
    for i in range(1, 13):
        print("{:2} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f}".format(i, sval1, sval2, sval3, sval4, sval5, salary_pre-sval1-sval2-sval3-sval4-sval5-month1[i-1], month1[i-1]))
    year = round(sum(month1), 2)
    print(year)
    month = [round(i, 2) for i in month1]
    print(month)

#填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
tax(28800, 0.08, 0.02, 0.005, 0.12, 1000)





