sal=input('enter the salary: ')

print('Gross Salary:')

gs=0

if int(sal)<10000 :

   hra=0.67*int(sal)

   da=0.73*int(sal)

elif int(sal)>=10000 & int(sal)<=20000:

   hra = 0.69* int(sal)

   da = 0.76* int(sal)

else int(sal)>20000:

   hra = 0.73* int(sal)

   da = 0.89 * int(sal)

gs = hra + da + int(sal)

print(gs)