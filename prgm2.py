yr=int(input("enter the future year"))
for i in range(2021,yr+1):
   if i%4==0 and i%100!=0 or i%400==0:
       print(i)