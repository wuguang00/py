#!/usr/bin/python3
# usage like below: input 0 or 1
# $ ./salary.py 0 # 
# $ ./salary.py 1 # Contain 补充公积金
# 2022, Shanghai, Shebao and Gongjj

import sys
import os

os.system("chmod go-r ./shanghai_payment.py")

if len(sys.argv) <= 1:
    print("Usage:")
    print("./salary.py 0")
    print("./salary.py 1")
    exit()

# 填入税前月薪, 年终奖, 每月专项扣除
pay_mon       = 95000
year_awards   = 300000
deduction_mon = 2000

sval = []
tax_mp = 0
get_mon = []
def tax(before_tax, deduction):
    """根据税前月薪, 社保, 医疗保险, 失业保险, 公积金, 专项扣除 算出2022每月应交税额"""
    # 公积金: 4786, %7 补充公积金: 3418, 5%

    sval   = before_tax
    salmax = 34188 # https://shgjj.com/html/zyxw/209768.html
    shebao = 0
    yiliao = 0
    shiye  = 0
    gongjj = 0
    bcgjj  = 0

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
        temp = before_tax - shebao - yiliao - shiye - gongjj - bcgjj - 5000 - deduction
    else:
        temp = before_tax - shebao - yiliao - shiye - gongjj - 5000 - deduction
        bcgjj = 0

    print("")
    print("pension_insurance:       {:.2f}".format(shebao))
    print("medical_insurance:       {:.2f}".format(yiliao))
    print("unemployment_insurance:  {:.2f}".format(shiye))
    print("housing_fund:            {:.2f}".format(gongjj + bcgjj))
    print("")
    
    month_temp = []
    count = 0
    # 计算新税
    for i in range(0, 12):
        k = int(temp * (i + 1))
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
        month_temp.append(temp * (i + 1) * rate_tax - part_tax - count)
        count += month_temp[i]
        get_mon.append(before_tax - shebao - yiliao - shiye - gongjj - month_temp[i])
        print("The {:2}, you get the salary: {:8.2f} with tax {:8.2f}".format(i + 1, get_mon[i], month_temp[i]))
        
    print("")
    print("     社保    医疗保险 失业保险  公积金  补充公积金    税后     缴税")
    for i in range(0, 12):
        print("{:2} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:12.2f} {:8.2f}".format(i + 1, shebao, yiliao, shiye, gongjj, bcgjj, before_tax-shebao-yiliao-shiye-gongjj-bcgjj-month_temp[i], month_temp[i]))
    tax_mp = round(sum(month_temp), 2)
    print(tax_mp)
    month = [round(i, 2) for i in month_temp]
    print()
    print("每月个税: {}".format(month))
    print()
    print("全年月薪个人所得税: {:8.2f}".format(tax_mp))
#填入税前月薪, 社保: 养老, 医疗, 失业, 公积金, 每月专项扣除
tax(pay_mon, deduction_mon)

# <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
# 个人所得税奖金单独计税. 综合计税.

tax_ya = 0
per_month = year_awards / 12    

if   0 <     per_month <= 3000:
    tax_ya = year_awards * 0.03
elif 3000  < per_month <= 12000:
    tax_ya = year_awards * 0.10 - 210
elif 12000 < per_month <= 25000:
    tax_ya = year_awards * 0.20 - 1410
elif 25000 < per_month <= 35000:
    tax_ya = year_awards * 0.25 - 2660
elif 35000 < per_month <= 55000:
    tax_ya = year_awards * 0.30 - 4410
elif 55000 < per_month <= 80000:
    tax_ya = year_awards * 0.35 - 7160
elif 80000 < per_month:
    tax_ya = year_awards * 0.45 - 15160
else:
    print("    别闹！\n    别闹！\n    别闹！\n")
    exit()
# 个人所得税奖金单独计税. 综合计税.
print("")
print("年终奖税后实发: {:8.2f} 年终奖税后实发: {:8.2f} 个人所得税奖金单独计税: {:8.2f}".format(year_awards, year_awards - tax_ya, tax_ya))
print("")
print("All your pay: {:8.2f}".format(sum(get_mon) + year_awards - tax_mp - tax_ya))
    

    
            
        
    
    
 
 
 
 
 
 
 
   
        
        
        
        
        
        
        
        
    
    
