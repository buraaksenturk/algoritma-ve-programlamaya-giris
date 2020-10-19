########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#          Boş bir listeye 0 ile 200 arasında          #
#                  10 sayı yazdırınız.                 #
#           Bu sayıların ortalamasını bulunuz.         #
#       Sonucu masaüstünde bir dosyaya yazdırınız.     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import random
a=[]
toplam=0
for i in range(10):
    sayi=random.randrange(0,200)
    print(sayi)
    a=a+[sayi]
    toplam=toplam+sayi
    ortalama=toplam/10
print(a)
print(ortalama)

veri=open("metin.txt","a")
veri.write(str(a))
veri.write(str(ortalama))
veri.close()


