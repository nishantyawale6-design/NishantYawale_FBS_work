# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

basic_sal = int(input('enter the basic salary: '))
da_per = float(input('enter the da_amt in percentage : '))
ta_per = float(input('enter the ta_amt in percentage: '))
hra_per = float(input('enter the hra_amt in percentage: '))

da_amt = basic_sal *  da_per/100 
ta_amt = basic_sal * ta_per/100
hra_amt = basic_sal * hra_per/100

total_sal = basic_sal + da_amt + ta_amt + hra_amt

print(f'the total sallary of employe is {total_sal}.')