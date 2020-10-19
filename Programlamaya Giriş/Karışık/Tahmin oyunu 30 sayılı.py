########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                Tahmini seçilen 30 sayıdan            #
#          tek olanları ve çift olanları toplayıp      #
#     teklerin çiftlerden kaç fazla olduğunu bulunuz.  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import random
tekt=0
ciftt=0
for i in range(30):
    sayi=random.randrange(1,100)
    print("Girilen sayı:",sayi)
    if sayi%2==0:
        ciftt=ciftt+sayi
    else:
        tekt=tekt+sayi
    print("tek sayıların toplamı",tekt)
    print("çift sayıların toplamı",ciftt)
print(ciftt-tekt)
    

