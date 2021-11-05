# 5) Payroll Calculator
# Getting wages & no: of days worked from employee
wages = float(input("Enter the wages : "))
days_worked = int(input("Enter the no: of days worked : "))
#calculating the pay & allowance of employee
basic_pay = wages*days_worked
hra = (basic_pay/100)*10
da = (basic_pay/100)*5
pf = (basic_pay/100)*12
net_pay = basic_pay + hra + da + pf
print("Basic Pay : ",basic_pay,"\nHRA : ",hra,"\nDA : ",da,"\nPF : ",pf,"\nNet Pay : ",net_pay)

