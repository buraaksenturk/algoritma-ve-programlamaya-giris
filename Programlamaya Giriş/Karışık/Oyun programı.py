########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                      #
#                    OYUN PROGRAMI                     #
#                                                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import random

puan=0
def uret():
    global toplam
    sayibir=random.randrange(1,10)
    sayiiki=random.randrange(1,10)
    toplam=sayibir+sayiiki
    print(sayibir,"+",sayiiki,"=?")
uret()
cevap=int(input("Toplama İşlemini Tahmmin Ediniz:"))
tekrar=""
while tekrar!="h":
    if cevap==toplam:
        print("Tebrikler Bildiniz :D")
        puan=puan+5
        print("Puanınız:",puan)
        tekrar=input("Tekrar Oynamak İstiyor Musunuz? evet=e,hayır=h")
        if tekrar=="e":
            uret()
            cevap=int(input("Toplama İşlemini Tahmin Ediniz:"))
        if tekrar=="h":
            print("Oyun Bitti. Toplam Puanınız:",puan)
    if cevap!=toplam:
        print("Yalnış cevap verdiniz")
        puan=puan-2
        print("Puanınız:",puan)
        uret()
