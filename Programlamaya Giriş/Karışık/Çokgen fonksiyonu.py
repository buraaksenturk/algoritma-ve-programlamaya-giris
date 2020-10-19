########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               Çokgen fonksiyonu oluşturup            #
#                   uzunluk,açı ve kenar               #
#             değerleri ile fonk tanımlayınız.         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

import turtle
kenar=int(input("kenar değeri giriniz:"))
uz=int(input("uzunluk giriniz:"))
aci=int(input("aci giriniz:"))
def çokgen(uz,aci,kenar):
    for i in range(kenar):
        turtle.fd(uz)
        turtle.lt(aci)

çokgen(uz,aci,kenar)
