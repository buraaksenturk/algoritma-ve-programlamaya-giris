########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               Klavyeden girilen 10 sayıdan           #
#           pozitif ve negatif olanların toplamını     #
#              ekrana yazan programı yazınız.          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

ps=0
ns=0
for i in range(10):
    a=int(input("Sayı giriniz"))
    if a>0:
        ps=ps+a
    elif a<0:
        ns=ns+a
print("Pozitif sayı toplamı",ps)
print("Negatif sayı toplamı",ns)
