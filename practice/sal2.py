#!/usr/bin/env python3

# 2021, Shanghai
# base max: 28017

# Terminology:
# social insurance
# endowment insurance         : 养老保险       , emi
# medical insurance           : 医疗保险       , mdi
# housing accumulation fund   : 住房公积金     , haf
# supplementary housing_fund  : 补充住房公积金 , shf
# unemployment insurance      : 失业保险       , uei
# employment injury insurance : 工伤保险       , eii
# maternity insurance         : 生育保险       , mni

# deduction of surcharges on specialized items : 专项附加费扣除 , ded

import argparse

num  = []
sval = []

argpar = argparse.ArgumentParser(description = '%(prog) help:')
argpar.add_argument('--bcg', dest = 'bcg', action = 'store_true', default = True, help = 'Do you have bu chong gong ji jin. Eg. --bcg')
argpar.add_argument('--pay', dest = 'pay', action = 'store', help = '')

args = argpar.parse_args()

# 填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 专项扣除

toplimit  = 28017 # 2021 June, 31014,
sal_mon   = 28800 
pay_raise = 5600

pay_arr = [
    sal_mon,                    # 1  月 "Jan" : 
    sal_mon,                    # 2  月 "Feb" : 
    sal_mon,                    # 3  月 "Mar" : 
    sal_mon,                    # 4  月 "Apr" : 
    sal_mon + pay_raise * 2,    # 5  月 "May" : 
    sal_mon + pay_raise,        # 6  月 "Jun" : 
    sal_mon + pay_raise,        # 7  月 "Jul" : 
    sal_mon + pay_raise,        # 8  月 "Aug" : 
    sal_mon + pay_raise,        # 9  月 "Sep" : 
    sal_mon + pay_raise,        # 10 月 "Oct" : 
    sal_mon + pay_raise,        # 11 月 "Nov" : 
    sal_mon + pay_raise         # 12 月 "Dec" : 
]

def insurance(base, rate):
    global toplimit
    act_val = 0
    temp_arr = []
    if (base > toplimit):
        act_val = round(toplimit * rate)
    else:
        act_val = round(base*rate, 2)
    for i in range(0, 12):
        temp_arr.append(act_val)
    return temp_arr

emi_arr = []
mdi_arr = []
uei_arr = []
haf_arr = []
shf_arr = []
ded_arr = []

g = lambda x,y: insurance(x, y)

emi_arr = g(sal_mon, 0.08)
mdi_arr = g(sal_mon, 0.02)
uei_arr = g(sal_mon, 0.005)
haf_arr = g(sal_mon, 0.07)
shf_arr = g(sal_mon, 0.05)
ded_arr = g(1000, 1)

print(emi_arr)
print(mdi_arr)
print(uei_arr)
print(haf_arr)
print(shf_arr)
print(ded_arr)

# You can edit them manually to replace the automatic one
# emi_arr = [2241, 2241, 2241, 2241, 2241, 2241, 2241, 2241, 2241, 2241, 2241, 2241]
# mdi_arr = [560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560]
# uei_arr = [140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140]
# haf_arr = [1961, 1961, 1961, 1961, 1961, 1961, 1961, 1961, 1961, 1961, 1961, 1961]
# shf_arr = [1401, 1401, 1401, 1401, 1401, 1401, 1401, 1401, 1401, 1401, 1401, 1401]
# pay_arr = [33600, 33600, 33600, 124600, 33600, 33600, 33600, 33600, 33600, 33600, 33600, 67200]

montax_countin = []
mon_tax = []
mon_tax = []

count   = 0
tax_countin = 0
actual_tax_mon = 0

for i in range(0, 12):
    tax_countin = pay_arr[i] - emi_arr[i] - mdi_arr[i] - uei_arr[i] - haf_arr[i] - 5000 - ded_arr[i]
    if args.bcg == True:
        tax_countin = tax_countin-  shf_arr[i]
    count += tax_countin
    if 0 <= count <= 36000:
        rate_tax = 0.03
        part_tax = 0
    elif 36000 < count <= 144000:
        rate_tax = 0.1
        part_tax = 2520
    elif 144000 < count <= 300000:
        rate_tax = 0.2
        part_tax = 16920
    elif 300000 < count <= 420000:
        rate_tax = 0.25
        part_tax = 31920
    elif 420000 < count <= 660000:
        rate_tax = 0.3
        part_tax = 52920
    elif 660000 < count <= 960000:
        rate_tax = 0.35
        part_tax = 85920
    elif count > 960000:
        rate_tax = 0.45
        part_tax = 181920
    else:
        raise ValueError("Negative value is not supported.")

    montax_countin.append(tax_countin)
    actual_tax_mon = count * rate_tax - part_tax - sum(mon_tax)
    mon_tax.append(round(actual_tax_mon, 2))
    print("tax counted in - {0:2}: {1:.2f}".format(i, montax_countin[i]))

print("")
print("    社保       医疗保险   失业保险   公积金     补充公积金  税后       缴税")
for i in range(0, 12):
    print("{:3} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<11.2f} {:<10.2f} {:<10.2f}".format(i, \
     emi_arr[i], mdi_arr[i], uei_arr[i], haf_arr[i], shf_arr[i], montax_countin[i]-emi_arr[i]-mdi_arr[i]-uei_arr[i]-haf_arr[i]-shf_arr[i]-mon_tax[i], mon_tax[i]))
year = round(sum(mon_tax), 2)
print()
print("TAX-all: {0}".format(year))
print()
month = [round(i, 2) for i in mon_tax]
print(month)
print("")



