x=[10,20,30,[50,60]]
index=0
index1=0
for i in x:
  if i==x[3]:
    for i in x[3]:
       print(index,' ',index1,' ',i)
       index1=index1+1
  else:
   print(index,'     ',i)
   index=index+1
