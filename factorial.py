#name Sreeraj Karpe
#roll no. 28
#gr no 11810158


def factor(x): 
   if x==0:
      print("0")
   elif x==1:
      print("1")
   else:
      multi=1
      for i  in range (2,x+1,1):
        multi=multi*i
      print(multi)
x=int(input("enter a number"))
m=factor(x)
