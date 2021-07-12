#!/usr/bin/env python3

import argparse

# 2021, Shanghai

pem = 28000 # pem: salary per month
bmx = 28017 # bmx: base max: 28017
edm = 0     # edm: endowment insurance         社保
med = 0     # med: medical insurance           医疗保险
une = 0     # une: unemployment insurance      失业保险
            # emp: employment injury insurance 工伤保险
mat = 0     # mat: maternity insurance         生育保险金
hou = 0     # hou: housing provident fund      住房公积金
sup = 0     # sup: supplementary housing fund  补充公积金

edu = 1000  # edu: the special expense education

argpar = argparse.ArgumentParser(description = '%(prog) help:')
argpar.add_argument('--sup', dest = 'sup', action = 'store_true', help = 'Do you have supplementary housing fund. Eg. --sup')
argpar.add_argument('--pem', dest = 'pem', action = 'store', help = 'salary per month')
args = argpar.parse_args()

if args.pem != None:
    pem = int(args.pem)

pem = 33600
bmx = 28017 # For Shanghai's maximum value
edm = 0
med = 0
une = 0
hou = 0
sup = 0    

edu = 1000 

cal_tax_pem = 0

if pem <= 28017:
    [edm, med, une, hou, sup] = [0.08 * pem, 0.02 * pem, 0.005 * pem, 0.07 * pem, 0.05 * pem]
else:
    [edm, med, une, hou, sup] = [0.08 * bmx, 0.02 * bmx, 0.005 * bmx, 0.07 * bmx, 0.05 * bmx]

if args.sup == True:
    cal_tax_pem = pem - edm - med - une - hou - sup - 5000 - edu
else:
    cal_tax_pem = pem - edm - med - une - hou - 5000 - edu
    sup = 0

ml_act = []
ml_cal = []

for i in range(1, 13):
    ml_act.append(pem)
    ml_cal.append(cal_tax_pem)

ml_act = [pem, pem, pem, pem, pem, pem, pem, pem, pem, pem, pem, pem]
for i in range(0, 12):
    ml_cal[i] = ml_act[i] - cal_tax_pem

print(ml_act)
print(ml_cal)


# 计算新税
# # 填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
# def tax(pem, edm, med, une, hou, edu):
#     """根据税前月薪, 社保, 医疗保险, 失业保险, 公积金, 专项扣除
#     算出2020每月应交税额"""
# 
#     for i in range(0, 12):
#         k = int(cal_tax_pem * (i+1))
#         if k <= 0:
#             rate_tax = 0
#             part_tax = 0
#         elif 0 < k <= 36000:
#             rate_tax = 0.03
#             part_tax = 0
#         elif 36000 < k <= 144000:
#             rate_tax = 0.1
#             part_tax = 2520
#         elif 144000 < k <= 300000:
#             rate_tax = 0.2
#             part_tax = 16920
#         elif 300000 < k <= 420000:
#             rate_tax = 0.25
#             part_tax = 31920
#         elif 420000 < k <= 660000:
#             rate_tax = 0.3
#             part_tax = 52920
#         elif 660000 < k <= 960000:
#             rate_tax = 0.35
#             part_tax = 85920
#         elif k > 960000:
#             rate_tax = 0.45
#             part_tax = 181920
# 
#         month1.append(cal_tax_pem * i * rate_tax - part_tax - count)
#         count += month1[i-1]
#         print("TAX - {0:<2}: {1:.2f}".format(i, count))
# 
#     print("")
#     print("    社保       医疗保险   失业保险   公积金     补充公积金  税后       缴税")
#     for i in range(1, 13):
#         print("{:3} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<11.2f} {:<10.2f} {:<10.2f}".format(i, edm, med, une, hou, sup, pem-edm-med-une-hou-sup-month1[i-1], month1[i-1]))
#     year = round(sum(month1), 2)
#     print()
#     print("TAX-all: {0}".format(year))
#     print()
#     month = [round(i, 2) for i in month1]
#     print(month)
#     print("")
# 
# #填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除
# print()
# tax(33600, 0.08, 0.02, 0.005, 0.12, 1000)



        # print("{}:pension_insurance:       {}".format(i, edm))
        # print("The {}, you get the salary: {:.2f}".format(i, pem - edm - med - une - hou - month1[i-1]))



