mlist=[1,2,3,4,5,6,7,8,9,12,15,16,18,20,22,24,26,28,30]
for i in mlist:
    if i%2==0:
       mlist.remove(i)
print(mlist)