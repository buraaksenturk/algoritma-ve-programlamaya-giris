########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                Tahmini bir sayı seçtirip             #
#                  sayıyı bulmaya çalışma              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import random
a=random.randrange(1,100)
tahmin=int(input("Tahmini bir sayı giriniz:"))
while tahmin!=a:
    if tahmin>a:
        print("Daha küçük bir sayı giriniz:")
    if tahmin<a:
        print("Daha büyük bir sayı giriniz:")
    tahmin=int(input("SAYI GİRİNİZ:"))
    if tahmin==a:
        print("TEBRİKLER BULDUNUZ..")
