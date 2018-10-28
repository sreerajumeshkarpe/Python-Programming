#name Sreeraj Karpe
#roll no. 28
#gr no 11810158
from random  import randint as rt
out=0
faces=6
dice=1
for roll in range(0,dice):
    out+=rt(1,faces)
print(out)