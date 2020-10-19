########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   Rastgele 30 sayıdan                #
#            5'e ve 7'ye bölünebilen sayıları          #
#   bunların toplamını ve ortalamasını bulan program   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import random
toplam=0
sayac=0
for i in range(30):
    a=random.randrange(1,1000)
    if a%5==0:
        print("5e bölünebilen sayılar",a)
        toplam=toplam+a
        sayac=sayac+1
        ort=toplam/sayac
    if a%7==0:
        print("7 ye bölünebilen sayılar",a)
        toplam=toplam+a
        sayac=sayac+1
        ort=toplam/sayac
print("5e ve 7ye bölünebilenlerin toplamı",toplam)
print("ortalaması",ort)
