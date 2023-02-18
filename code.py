import numpy as np
hours=np.array([0,0,0,0,0,0,0])
pay_weekly_overtime=0
pay_weekday=0
pay_weekend=0
days={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
for i,j in days.items():
    hours[j]=int(input(f"Enter number of working  hours in {i}"))
    if(hours[j]>24):
        print("Wrong Entry")
        hours[j]=int(input(f"Please reenter number of working  hours in {i}"))
    else:
        pass
_sum=sum(hours)-hours[0]-hours[6]
pay_weekend=( hours[0] + hours[6] ) * 2.0
for i in range(1,6):
    if( hours[i] > 8 ):
        pay_weekday += ( hours[i] - 8 ) * 2.0
        pay_weekday += 8.0
    else:
        pay_weekday += hours[i] * 1.0
if(_sum>30):
    pay_weekly_overtime = ( _sum - 30 ) * 1.5
payroll=pay_weekend + pay_weekday + pay_weekly_overtime
print("Employee payroll = ", payroll)
